import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.decorators.cache import never_cache
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from spa.models import Notes


@never_cache
@csrf_protect
def spa(request):
    return render(request, 'spa.html')


class DetailView(generic.DetailView):
    """
    Встроенный класс для отображения детальных записей
    """
    model = Notes
    template_name = 'notes_detail.html'


def notes(request):
    """
    GET запрос списка всех записей из БД
    :param request: контекст запроса (подставляет Django)
    :return: json содержащий массив элементов Notes
    """
    note_list = list(Notes.objects.all().values())
    return JsonResponse(note_list, safe=False)


@require_POST
def save(request):
    """
    POST запрос на запись тела запроса в БД
    :param request: контекст запроса (подставляет Django)
    :return: возвращает ответ об окончании записи в БД
    """
    body = json.loads(request.body)
    try:
        note = Notes.objects.get(pk=body['date'])
    except Notes.DoesNotExist:
        note = Notes(date=body['date'])
    else:
        note.title = body['title']
        note.note = body["note"]
        note.save()

    return HttpResponse('note update')
