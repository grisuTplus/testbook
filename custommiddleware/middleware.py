__author__ = 'grisu'

from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from testbook.customuser.models import CustomUser

import re

class RequireLoginMiddleware(object):
    def __init__(self):
        self.exceptions = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS])

    def process_request(self, request):
        if request.user.is_authenticated(): return None

        for url in self.exceptions:
            if url.match(request.path):
                return None

        if request.user.is_anonymous():
            return HttpResponseRedirect('/login')