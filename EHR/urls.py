"""
URL configuration for EHR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from Home import views as hviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    #~~~~~~~~~~~~~~~~~~~
    path('',hviews.home,name="home"),

    path('index/',hviews.index,name="index"),
    path('about/',hviews.about,name="about"),
    path('contact/',hviews.contact,name="contact"),
    path('gallary/',hviews.gallary,name="gallary"),
    path('faq/',hviews.faq,name="faq"),
    path('add/',hviews.add,name="add"),
    path('mul/',hviews.mul,name="mul"),
    path('calculator/',hviews.calculator,name="calculator"),

    # Register
    path('register/', include('Register.urls')),
    # Contact
    path('cont/', include('Contact.urls')),
    # login
    path('login/',include('login.urls')),
    # logout
    path('logout/',include('Logout.urls')),
    # ehrAdmin
    path('ehradmin/', include('EhrAdmin.urls')),
    # # Doctor
    path('doctor/', include('Doctor.urls')),
    # # Staff
    path('staff/',include('Staff.urls')),
    # Patient
    path('patient/',include('Patient.urls')),

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

