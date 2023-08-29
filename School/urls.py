from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_header='NBV School Portal'
admin.site.site_title='NBV Adminstration'
admin.site.index_title='Welcome to NBV Portal'
urlpatterns=[
    path('', views.index),
    path('/', views.home),
    path('aboutus', views.aboutus),
    path("contact", views.contact),
    path("events", views.events),
    path("courses", views.course),
    path("classes/<str:class_name>/", views.classes, name='class_page'),
]