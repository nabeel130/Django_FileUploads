"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fileuploads.views import Home ,upload ,book_list , upload_book ,BookList ,UploadBookView ,delete_book
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view() ,name = 'home'),    
    path('upload/', upload ,name = 'upload'),
    path('books/', book_list ,name = 'book_list'),
    path('books/upload/', upload_book ,name = 'upload_book'),
    path('class/books/', BookList.as_view() ,name = 'class_book_list'),
    path('class/books/upload/', UploadBookView.as_view() ,name = 'class_upload_book'),
    path('books/<int:pk>', delete_book ,name = 'delete_book'),
   
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
