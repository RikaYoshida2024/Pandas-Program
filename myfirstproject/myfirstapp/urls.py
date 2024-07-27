from django.contrib import admin
from django.urls import path
from myfirstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about',views.myfunctionabout,name="about"),
    path('success-page',views.success_page, name="success_page")
]