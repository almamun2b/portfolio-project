from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Optional for include
# from jobs.views import home
# from jobs import views
# import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("jobs.urls"), name='home'),
    path('blog/', include("blog.urls"), name='blog'),

    # path('', home, name='home'),
    # path('', views.home, name='home'),
    # path('', jobs.views.home, name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
