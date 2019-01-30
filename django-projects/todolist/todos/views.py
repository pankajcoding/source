# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.

def index(req):
	todos=Todo.objects.all()[:10]

	context={
	"todos":todos
	}

	return render(req,'index.html',context)

def details(req,id):
	todo=Todo.objects.get(id=id)
	context={
		"todo":todo
	}

	return render(req,'detail.html',context)

def add(req):
	if req.method=='POST':
		title=req.POST['title']
		text=req.POST['text']
		todo=Todo(title=title,text=text)
		todo.save()
		return redirect('/todos')
	else:	
		context={}
		return render(req,'add.html',context)