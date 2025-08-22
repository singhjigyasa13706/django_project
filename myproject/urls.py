from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),  # or views.index if you prefer
    path('blog/', include('blog.urls')),            # This enables /blog/ URLs
]
