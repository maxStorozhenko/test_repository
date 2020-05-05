from django.http import HttpResponse

from django.shortcuts import render  # noqa  Autoimported by django

from group.models import Group


def show_groups(request) -> HttpResponse:
    groups = Group.objects.all()
    response = ''
    for group in groups:
        response += group.info() + '<br/>'
    return HttpResponse(response)
