import datetime
import logging
import os
import urllib
from urlparse import urlparse, parse_qs, urlsplit, urlunsplit

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.encoding import smart_str
from django.views.generic import TemplateView, View

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from braces.views import JSONResponseMixin, AjaxResponseMixin
# https://django-braces.readthedocs.org/



def index(request):
	return render_to_response('base.html', context_instance=RequestContext(request))