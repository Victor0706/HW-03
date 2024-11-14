from django.urls import path
from .views import RegisterUser, ProfileUser, LoginUser, ProfileList
from django.contrib.auth.views import LogoutView
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
    path('', views.index, name='index'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile', ProfileUser.as_view(), name='profile'),
    path('profile_list', ProfileList.as_view(), name='profile_list'),
    path('accounts/login', LoginUser.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

