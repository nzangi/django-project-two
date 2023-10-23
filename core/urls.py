from . import views
from django.urls import path
app_name='core'
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('contact/', views.contact, name='contact'),

]