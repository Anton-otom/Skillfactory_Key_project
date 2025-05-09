from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('forum/', include('Forum_board.urls')),
]
