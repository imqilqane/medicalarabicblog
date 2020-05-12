from django.shortcuts import render , get_object_or_404
from .models import Post
from .forms import new_comment
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

def home (request):
   posts = Post.objects.all()
   paginator = Paginator(posts,5)
   page =request.GET.get('page')
   try:
      posts = paginator.page(page)
   except PageNotAnInteger :
      posts = paginator.page(1)
   except EmptyPage :
      posts = paginator.page(paginator.num_pages)

   context = {
      'title' : 'الصفحة الرئيسية',
      'posts': posts,
      'page' : page
   }
   return render(request, 'Blog/index.html', context)


def about (request):
   return render(request , 'Blog/about.html' , {'title' : 'حول'})


def detiels (request , post_id):
   post = get_object_or_404(Post ,pk=post_id)
   comments = post.comments.filter(active=True)
   comment_form = new_comment()

   context ={
      'title': post,
      'post':post,
      'comments':comments,
      'comment_form':comment_form,

   }
   if request.method == 'POST': #hna glna lo ila kant def katsaw POST
      comment_form = new_comment(data=request.POST) # st9bal lbayanat
      if comment_form.is_valid():
         NewComment = comment_form.save(commit=False) #hna kn9ol lih mazal madir save hitax mzl m3rfna had lcommint dyal axmn post
         NewComment.post = post #post lwla hya lvar f class dyal dyal comments f model
         NewComment.save()  # daba 3ad ndir save
         comment_form = new_comment()  # daba ndir tafrigh llform
   else:
      addComment = new_comment()
   return render(request, 'Blog/post_detiels.html' , context)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
   model = Post
   fields = ('title' ,'content' ,'image')
   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)
   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
         return True
      else:
         return False

class DeletPost(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
   model = Post
   success_url = '/'
   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
         return True
      else:
         return False
# Create your views here.
