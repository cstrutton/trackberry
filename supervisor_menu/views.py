from django.shortcuts import render
from .models import SupervisorMenuItem, SupervisorSubMenuItem


def index(request):

    top_items = SupervisorMenuItem.objects.order_by('position').all()
    sub_items = SupervisorSubMenuItem.objects.order_by('position').all()
    menu_list = []
    for item in top_items:
        menu_item = {'text': item.text,
                     'url': item.url,
                     'submenus': []}
        for sub_item in sub_items.filter(parent_id=item.id).order_by('position').all():
            menu_item['submenus'].append({'text': sub_item.text,
                                          'url': sub_item.url})

        menu_list.append(menu_item)

    return render(request, 'index.html', context={'menu_list': menu_list})
