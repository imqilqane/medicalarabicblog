from django.shortcuts import render , redirect
from .forms import UserCrationForm
from django.contrib import messages
from .forms import   UserCrationForm , Userupdateform , Proupdateform
from django.contrib.auth import authenticate , login
from Blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def register (request):

    if request.method == 'POST':
        signup_form = UserCrationForm(request.POST)  #glna lo ila kant def dyal lform hya POST idan lform ghadi ysr9b lbayanat mn request.POST
        if signup_form.is_valid():
            new_user = signup_form.save(commit=False)
            #username = signup_form.cleaned_data['username']
            new_user.set_password(signup_form.cleaned_data['password1'])
            new_user.save()
            messages.success(request , f'  تهانينا{new_user} لقد تم التسجيل بنجاح  ')
            return redirect('login')
    else:
        signup_form = UserCrationForm()  #ila ma th9a9x xart lfrom ghadi yb9a khawi


    return render(request, 'user/sign_up.html' ,  {
        'title': 'التسجيل',
        'signup_form' : signup_form,
        })

def loginUser (request):

    if request.method == 'POST':
        username = request.POST['username'] #hna kandiro cash llm3lomat li bghina db bghina user w pass
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #hna drna authenticate luser w pass wkhznnahom fvar
        if user is not None :
            login(request , user)#had user hna rah ghir var
            return redirect('profile')

        else:
            messages.warning(request , 'عذرا المعلمات التي ادخلت غير صحيحة')


    return render(request, 'user/login.html', {'title': 'تسجيل الدخول',  })

@login_required(login_url='login')
def profile (request):
    posts = Post.objects.filter(author=request.user)

    post_l = Post.objects.filter(author=request.user)
    paginator = Paginator(post_l, 2)
    page = request.GET.get('page')
    try:
        post_l = paginator.page(page)
    except PageNotAnInteger:
        post_l = paginator.page(1)
    except EmptyPage:
        post_l = paginator.page(paginator.num_pages)
    return render(request,'user/profile.html' , {'title': 'الملف الشخصي',
                                                 'posts':posts,
                                                 'page':page,
                                                 'post_l':post_l})

@login_required(login_url='login')
def Userupdate( request):
    if request.method == 'POST':
            user_form = Userupdateform(request.POST , instance=request.user)
            pro_form = Proupdateform(request.POST , request.FILES, instance=request.user.user_profile) #hitax had l7a9l kay3dal ta lmilafat
            if user_form.is_valid() and pro_form.is_valid():
                user_form.save()
                pro_form.save()
                messages.success(request,  '  تهانينا لقد تم تعديل الملف بنجاح  ')
                return redirect('profile')
    else:
            user_form = Userupdateform(instance=request.user)
            pro_form = Proupdateform(instance=request.user.user_profile)
    context = {
        'title' : 'تعديل الملف الشخصي' ,
        'user_form' : user_form,
        'pro_form' : pro_form,
    }
    return render(request , 'user/userupdate.html' , context)

class PostCreatView (LoginRequiredMixin ,CreateView):
    model = Post
    fields = ('title' , 'content' ,'image')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)