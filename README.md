# django_upload_download
Upload and Downlaod File in django(version 3 test and worked)
You can see tutorial in Youtube video or read documents.
https://youtu.be/MpDZ34mEJ5Y

###### in terminal
1.activate djangoenv
2.django-admin startproject upload_download
3.django-admin startapp core

4.in settings.py
TEMPALTE_DIR = os.path.join(BASE_DIR,'templates')
MEDIA_DIR = os.path.join(BASE_DIR,'media')

5. add core to INSTALLED_APP

6. add TEMPALTE_DIR in TEMPLATES_DIR

7.
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

8. Create templates folder as same location of core folder or manange.py
#create core folder inside templates dir
#Create index.html inside core folder
# Create media folder as same location of core folder or manange.py


9.models.py
class FileHandler(models.Model):

    
    file_upload = models.FileField(upload_to=file_path,validators=[validate_correspondence_file_extension],null=True,blank=True)


def file_path(instance, filename):
    path = "documents/"
    format = 'uploaded-' +  filename
    return os.path.join(path, format)


10.
###### in terminal
#make migrations core
# migrate

11.
#forms.py
from django import forms
from core.model import FileHandler
class FileHandlerForm(forms.ModelForm):

    file_upload =  forms.FileField()

    class Meta():
        model = FileHandler
        fields = ('correspondnce_file_upload')

12.
# urls.py
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

path('',include('core.urls'))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

13.
# core/urls.py
from core import views

app_name = 'core'
urlpatterns = [
	path('',views.IndexView.as_view(),name='index'),
]

14.
#views.py
from django.views.generic import TemplateView
from core.models import FileHandler
from core.forms import FileHandlerForm

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self,**kwargs):
        6:15 PM 4/16/2021
	context = {'form':FileHandlerForm}
        return context

    def post(self,request,**kwargs):
        context = {}
        if request.method== 'POST':
            
            form = FileHandlerForm(request.POST,request.FILES)
            if form.is_valid():
                FileHandler.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))
                return redirect('core:index')
            else:
                context['form'] = form
        else:
            context['form'] = form
        return redirect('core:index')


15.
# index.html

<form method="POST"  enctype="multipart/form-data">
    {% csrf_token %}
                      
    {{ form.file_upload|add_class:"form-control"|attr:"accept:.pdf" }}
    <button class="btn btn-primary" type="submit"></button>
    {{ form.errors }}
    {{ form.non_field_errors }}
                      
</form>
