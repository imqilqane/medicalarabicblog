from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('sign_up/' ,views.register , name='sign_up'),
    path('login/' ,views.loginUser, name='login'),
    #path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('login/', views.loginUser, name='login'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.Userupdate, name='editprofile'),
    path('newpost/', views.PostCreatView.as_view(template_name='user/newpost.html'), name='newpost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)