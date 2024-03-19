
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('savedpost.urls')),
    path('', include('likes.urls')),
    path('', include('friends.urls')),
]