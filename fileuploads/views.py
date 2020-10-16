from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.


from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'fileuploads/home.html'

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name , uploaded_file)
        url = fs.url(name)
        context = {
            'url' : url
        }
    return render(request, 'fileuploads/upload.html' , context)
    