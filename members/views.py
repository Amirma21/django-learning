from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from members.models import Member


def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template('membersList.html')
    context = {'my_members': my_members}
    return HttpResponse(template.render(context , request))