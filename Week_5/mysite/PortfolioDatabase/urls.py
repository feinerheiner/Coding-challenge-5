from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('hobbies/', views.Hobbies, name='hobbies'),
    path('contact/', views.Contact, name='contact'),
    path('css/', views.Portfolio, name='css'),
    path('hobbies/<int:item_id>', views.hobby_detail, name='detail'),
    path('css/<int:item_id>', views.project_detail, name='pdetail'),
]

