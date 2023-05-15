from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   # path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('muskayit/<int:pk>', views.customer_rec, name='Record'),
    path('delete_mus/<int:pk>', views.delete_customer_rec, name='sil_mus'),
    path('mus_ekle/', views.mus_ekle, name='musekle'),
    path('update-mus/<int:pk>', views.update_mus, name='update-mus'),

]
