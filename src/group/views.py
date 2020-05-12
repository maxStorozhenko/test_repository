from django.shortcuts import get_object_or_404, redirect, render, reverse

from forms import GroupCreateForm

from group.models import Group


def show_groups(request):
    groups = Group.objects.all()
    count = groups.count()
    return render(request, 'groups-list.html', context={'groups': groups,
                                                        'count': count})


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('groups:list'))
    elif request.method == 'GET':
        form = GroupCreateForm()

    context = {
        'form_name': 'CREATE GROUP',
        'create_form': form
    }
    return render(request, 'create.html', context=context)


def edit_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(reverse('groups:list'))
    elif request.method == 'GET':
        form = GroupCreateForm(instance=group)

    context = {'edit_form': form,
               'group': group,
               }

    return render(request, 'edit-group.html', context=context)


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return redirect(reverse('groups:list'))
