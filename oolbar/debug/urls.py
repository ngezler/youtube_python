import re

from django.conf.urls.defaults import *
from django.conf import settings
import django.views.static

from debug import views

urlpatterns = patterns('',
    # This need if you want to see EXPLAIN of sql queries
    (r'^explain_query/$', views.explain_query),
)
