from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("get/id/", views.get_id),
    path("page/", views.page, name="page"),
    path("room/<str:pk>/", views.room, name="room")
]
7861