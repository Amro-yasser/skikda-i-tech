
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from evenements.views import evenements
from formations.views import formations
from club.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',index),
    path ('formations/',formations),
    path ('evenements/',evenements)
]

if settings.DEBUG:
    		urlpatterns += static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    		urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

