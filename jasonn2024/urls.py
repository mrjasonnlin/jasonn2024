"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
# from main import views
from django.conf.urls.static import static
from django.conf import settings

# from blog.settings import MEDIA_ROOT
# from django.views.static import serve

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('render.urls')),
                  path('upload_profile/', include('upload_profile.urls', namespace='upload_profile')),
                  path('account/', include('account.urls', namespace='account')),
                  path('article/', include('article.urls', namespace='article')),
                  #    path('upload/', include('upload.urls', namespace='upload')),
                  #    path('main/', include('main.urls', namespace='main')),
                  #    path('main/', include('main.urls')),
                  #    re_path('.*', views.main),
              ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)