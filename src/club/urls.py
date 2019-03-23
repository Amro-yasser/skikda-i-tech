
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from evenements.views import evenements
from formations.views import formations
from club.views import index
from projects.views import projets,project_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',index),
    path ('formations/',formations),
    path ('evenements/',evenements),
    path ('projets/',projets,name="project"),
    path ('project_detail<id>',project_detail,name="project-detail"),
    path('tinymce/', include('tinymce.urls')),
    
]

if settings.DEBUG:
    		urlpatterns += static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    		urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

