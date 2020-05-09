from django.http import HttpResponse
from django.shortcuts import redirect, render

from forms import GroupCreateForm

from group.models import Group


def show_groups(request) -> HttpResponse:
    groups = Group.objects.all()
    response = ''
    for group in groups:
        response += group.info() + '<br/>'
    return HttpResponse(response)


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {
        'form_name': 'CREATE GROUP',
        'create_form': form
    }
    return render(request, 'create.html', context=context)
