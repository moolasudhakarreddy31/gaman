from JobsInfo import views
from django.urls import path


urlpatterns = [
    path('home/',views.home),
    path('hydinfo/',views.hydjob),
    path('puneinfo/',views.punejobs),
    path('chennaiinfo/',views.chennaijobs),
    path('banginfo/',views.bangjobs),

]