"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import staticViewSitemap
from blog.sitemaps import blogSitemap
import debug_toolbar

sitemaps={
    'static': staticViewSitemap,
    'blog': blogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('url address' , view),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),

    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',include('robots.urls')),
    path('__debug__/',include(debug_toolbar.urls)),
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
