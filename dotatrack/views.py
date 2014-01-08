from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):
	# template = loader.get_template('templates/index.html')
	context = RequestContext(request, {})
	# template.render(context)
	# return HttpResponse(template.render(context))
	return render(request, 'dotatrack/index.html', context)

