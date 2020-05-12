from django import forms
from django.contrib.auth.models import User
from .models import user_profile
class UserCrationForm (forms.ModelForm):

    username = forms.CharField(label= 'اسم المستخدم', max_length=40 , help_text='اسم المستخدم لا يجب ان يحتوي على مسافات')
    email = forms.EmailField(label='البريد الاكتروني')
    first_name = forms.CharField(label= 'الاسم الاول')
    last_name = forms.CharField(label= 'اسم الاخير')
    password1 = forms.CharField(label= 'كلمة المرور', widget=forms.PasswordInput , min_length=8  , help_text='كلمة المرور يجب الا تقل عن 8 عناصر')
    password2 = forms.CharField(label= 'تأكيد كلمة المرور', widget=forms.PasswordInput , min_length=8 )

    class Meta :
        model = User
        fields = ('username','email','first_name','last_name','password1' ,'password2')

    def clean_password(self):
        cd = self.cleaned_data
        if cd ['password1']!= cd['password2']: #ila makantx lcleaned_data dyal psw1 = cd dya pass2 axghadi yw93
            raise forms.ValidationError('كلمة المرور غير متطابقة')#4adi ntl3o missag 3an tari9 forms 3abra ValidationError
        return cd ['password2']#hana fin bghini lmsg yban

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username =cd['username']).exists(): #hadi kat3NI ILA LUSER USERNAME KAYN MN0BL AX NDIR #KIMA KAT3RF USER 3NDO BZAF DYAL LWSOF DAKXI 3LAX KHASNI NST3ML LKWIRI BAX NFLITRI AXMN WHDA BGHIT
            raise forms.ValidationError('اسم المستخدم متواجد من قبل')
        return cd['username']

class Userupdateform (forms.ModelForm):

    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='اسم الاخير')
    email = forms.EmailField(label='البريد الاكتروني')

    class Meta:
        model = User
        fields = ('email','first_name','last_name' )

class Proupdateform (forms.ModelForm):

    class Meta:
        model = user_profile
        fields = ('image', )

