
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from evenements.views import evenements,events_details

from club.views import index
from projects.views import projets,project_detail,create_post,update_post,delete_post
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',index),
    path ('events_details/',events_details,name="events_details"),
    path ('evenements/',evenements,name="events"),
    path ('projets/',projets,name="project"),
    path ('project_detail/<id>/',project_detail,name="project-detail"),
    path ('create_post',create_post,name="create_post"),
    path ('project_detail/<id>/update_post',update_post,name="update_post"),
    path ('project_detail/<id>/delete_post',delete_post,name="delete_post"),
    
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    
]

if settings.DEBUG:
    		urlpatterns += static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    		urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

