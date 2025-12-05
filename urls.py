from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import ai_brain
import universities_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('test/', TemplateView.as_view(template_name='test.html'), name='test'),
    path('universities/', universities_views.universities_list, name='universities'),
    path('university/<str:slug>/', universities_views.university_detail, name='university_detail'),
    path('admin/', admin.site.urls),
    path('ai-chat/', ai_brain.ai_chat, name='ai_chat'),
    path('search-university/', ai_brain.search_university, name='search_university'),
]
