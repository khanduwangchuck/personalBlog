
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import  settings
from . import views

urlpatterns = [
    path('<str:pk>', views.profile, name='profile')

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)