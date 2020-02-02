from django.urls import path

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^pizzerias/$',PizzeriasViewSet.as_view(), name ='pizzerias'),
    url(r'^pizzerias/(?P<pk>[0-9]+)/$', PizzeriaDetail.as_view()),
    # path('snippets/', SnippetDetailView.as_view()),
]

