# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Supporter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def supporters_list(request):
    # groups = Group.objects.all()


    # #ordering groups
    # order_by = request.GET.get('order_by','')
    # groups=groups.order_by('title')
    # if request.GET.get('order_by','') == '':
    #     request.GET.order_by = 'title'

    # if order_by in ('leader', 'id','title'):
    #     groups=groups.order_by(order_by)
    #     if request.GET.get('reverse','')=='1':
    #         groups = groups.reverse()

    # #pagination

    # paginator = Paginator(groups, 3) # 

    # page = request.GET.get('page')
    # try:
    #     groups = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     groups = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     groups = paginator.page(paginator.num_pages)


    return HttpResponse('Good life')

def groups_add(request):
	return HttpResponse('<h1> group add form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1> Edit Groups %s </h1>' %gid)

def groups_delete(request, gid):
	return HttpResponse('<h1> Delete Groups %s </h1>' %gid)