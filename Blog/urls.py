from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import PostUpdateView ,DeletPost

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detiels/<int:post_id>/', views.detiels, name='detiels'),
    path('detiels/<slug:pk>/editpost/',PostUpdateView.as_view(template_name='Blog/editpost.html'), name='editpost'),
    path('detiels/<slug:pk>/deletpost/', DeletPost.as_view(template_name='Blog/deletpost.html'),  name='deletpost'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)