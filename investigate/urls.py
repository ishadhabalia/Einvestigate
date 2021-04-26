from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('investigationedit/<str:case>/', views.investigationedit, name = 'InvestigationEdit'),
path('investigationdetail/<str:case>', views.investigationdetail, name = 'InvestigationDetail'),
path('download/<str:file_name>', views.download, name='Download'),
] 
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns = patterns('',
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# ) + urlpatterns