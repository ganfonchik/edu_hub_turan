from django.shortcuts import render
from django.http import Http404
from universities_data import get_university, get_all_universities


def university_detail(request, slug):
    """Страница конкретного университета"""
    university = get_university(slug)
    
    if not university:
        raise Http404("Университет не найден")
    
    return render(request, 'university.html', {'university': university})


def universities_list(request):
    """Список всех университетов"""
    universities = get_all_universities()
    return render(request, 'universities_list.html', {'universities': universities})
