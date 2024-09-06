from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('Login.html', views.Login, name="Login"),
    path('profile', views.Profile, name = 'Profile'),
    path('Signup', views.Signup, name="Signup"),
    path("WebCam", views.WebCam, name="WebCam"),
    path('UserLogin', views.UserLogin, name="UserLogin"),
    path("saveSignup", views.saveSignup, name="saveSignup"),
    path('Admin.html', views.Admin, name="Admin"), 
    path('Register.html', views.Register, name="Register"),
    path('Admin_login', views.AdminLogin, name = 'AdminLogin'),
    path('upload', views.upload, name = "upload"),
    path("ValidateUser", views.ValidateUser, name="ValidateUser"),
    path("doc_upload", views.doc_upload, name = 'doc_upload'),
    path("adminPage", views.adminPage, name = 'adminPage'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('data_upload/', views.data_upload, name = 'data_upload'),
    path('view_doc/<str:username>/', views.view_doc, name = 'view_doc'),
    path('download/<path:file_name>/', views.download_file, name = 'download_file'),
]