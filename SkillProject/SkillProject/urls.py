from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('SkillDevelopmentPlatform.views.home'), name='home'),
]
