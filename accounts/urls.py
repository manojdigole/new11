
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register',register ,name='register'),
    #path('cal/',calu),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
#        urlpatterns += static(settings.MEDIA_URL,
 #                             document_root=settings.MEDIA_ROOT)