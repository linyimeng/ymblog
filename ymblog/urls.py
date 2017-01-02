from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #不能使用namespace='first'
    url(r'^admin/',include(admin.site.urls)),
    url(r'^',include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
