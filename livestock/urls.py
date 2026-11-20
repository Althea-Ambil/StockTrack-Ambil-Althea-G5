
from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.livestock_list,
        name="livestock_list"
    ),

    path(
        "add/",
        views.livestock_create,
        name="livestock_create"
    ),

    path(
        "edit/<int:pk>/",
        views.livestock_update,
        name="livestock_update"
    ),

    path(
        "delete/<int:pk>/",
        views.livestock_delete,
        name="livestock_delete"
    ),

]
