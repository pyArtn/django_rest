from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Artur's API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('', include('rest_framework.urls')),
    path('users/', include('apps.users.urls')),
    path('', include('apps.posts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
