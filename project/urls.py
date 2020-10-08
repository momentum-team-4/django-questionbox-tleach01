"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from questionbox.views import add_answer, question_detail, questions_list
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from users import views as users_views
from questionbox import views as questionbox_views
from questionbox.models import Question, Answer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', TemplateView.as_view(template_name="base.html")),

    path('questionbox/questions_list', questionbox_views.questions_list, name="questions_list"),
    path('quesionbox/question_detail', questionbox_views.question_detail, name='question_detail'),
    path('questionbox/add_question', questionbox_views.add_question, name="add_question"),
    path('questionbox/add_answer', questionbox_views.add_answer, name="add_answer"),

    path('users/create/', users_views.users_create, name='users_create'),
    path('users/login/', users_views.users_login, name='users_login'),
    path('users/logout/', users_views.users_logout, name='users_logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
