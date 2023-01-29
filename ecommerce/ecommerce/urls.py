"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.ContactUs,name='Contactus'),
    path('computer',views.computer,name='computer'),
    path('laptop',views.laptop,name='laptop'),
    path('washing_machine',views.washing_machine,name='washing_machine'),
    path('phone',views.phone,name='phone'),
    path('smarttv',views.smarttv,name='smarttv'),
    path('jeans',views.jeans,name='jeans'),
    path('product_detail/<str:category>/<int:id>/',views.product_detail,name='product_detail'),
    # path('product/<str:name>',views.productTemplate,name='product_template'),

    # new page with about name as below, and such we can tell as creating pipeline
    # path('about/',views.about,name='about')
    # and page not found 404 page means debug is true and if false then it will show only simple page not found page
    # path('RemovePunc',views.removepunc,name='removepunc'),
    # path('Captialize First',views.capfirst,name='Captialize First')

]

urlpatterns+=staticfiles_urlpatterns()

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)