from django.urls import path

from new_app2 import views

urlpatterns = [
    path("",views.dad,name="dad"),
    path("create",views.create,name="create")

]
