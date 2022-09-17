from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('contactus/', include('contact.urls')),
    # path('', views.index, name='index'),
    path('', include('index.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
