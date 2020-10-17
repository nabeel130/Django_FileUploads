from django.shortcuts import render , redirect
from django.views.generic import TemplateView , ListView , CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book

# Create your views here.


from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'fileuploads/home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name , uploaded_file)
        # url = fs.url(name)
        context['url'] = fs.url(name)
        context = {
           'url' : url
        }
    return render(request, 'fileuploads/upload.html' , context)



def book_list(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'fileuploads/book_list.html' , context)

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    context = {
        'form' : form
    }
    return render(request, 'fileuploads/upload_book.html' , context)


class BookList(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'




class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'fileuploads/upload_book.html'
    
    
    