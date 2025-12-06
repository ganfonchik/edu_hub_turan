from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
import ai_brain
import ai_compare
import universities_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('test/', TemplateView.as_view(template_name='test.html'), name='test'),
    path('universities/', universities_views.universities_list, name='universities_list'),
    path('universities/comparison/', TemplateView.as_view(template_name='comparison.html'), name='universities_comparison'),
    path('university/<str:slug>/', universities_views.university_detail, name='university_detail'),
    path('compare/', TemplateView.as_view(template_name='compare.html'), name='compare'),
    path('admin/', admin.site.urls),
    path('ai-chat/', ai_brain.ai_chat, name='ai_chat'),
<<<<<<< HEAD
    path('ai-compare/', ai_compare.ai_compare, name='ai_compare'),
=======
    path('search-university/', ai_brain.search_university, name='search_university'),
>>>>>>> 199c39e9235ecb1db1c45cf1a94ec073e7fde0b6
]
