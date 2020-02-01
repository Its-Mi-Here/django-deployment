from django.urls import path,include
from first_app import views


app_name = 'first_app'

urlpatterns = [
    #path('',views.index,name="index" ),
    path('relative/',views.relative,name="relative" ),
    path('users/',views.users,name="users" ),
    path('other/',views.other,name="other" ),
    
]