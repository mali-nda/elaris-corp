"""elaris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(),  name='home_view'),
    path('solutions', SolutionView.as_view(),  name='solutions_view'),
    path('about', AboutView.as_view(),  name='about_view'),
    path('contact', ContactView.as_view(),  name='contact_view'),
    path('thanks', thanks,  name='thanks_view'),
    path('thanks2', thanks2, name='thanks2_view'),
    path('joinus', joinus, name='join_view'),
    path('technology_partners', technology_partners, name='technology_partners'),
    path('job_detail/<int:myid>/', job_detail, name='job_detail'),
    path('job_apply/<int:myid>/', job_apply, name='job_apply'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
