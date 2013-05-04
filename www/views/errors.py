from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.template.context import RequestContext

def not_found(request):
    t = loader.get_template('errors/404.html')
    c = RequestContext(request, {'request_path': request.path})
    return HttpResponseNotFound(t.render(c))

def server_error(request):
    t = loader.get_template('errors/500.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c), status=500)
