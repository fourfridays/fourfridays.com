# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

from pages import views as page_views


urlpatterns = [
    url(r'^sales/$', page_views.sales_inquiry_form),
    url(r'^sales/inquiry/', page_views.sales_inquiry_hubspot_form),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)