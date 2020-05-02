from django.shortcuts import render
from django.http import HttpResponse
from group.models import Group


def show_groups(request) -> HttpResponse:
    groups = Group.objects.all()
    print(groups)
    response = ''
    for group in groups:
        response += group.info() + '<br/>'
    return HttpResponse(response)
