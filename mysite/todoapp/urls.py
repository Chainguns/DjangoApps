
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path('<int:id>/delete', views.remove, name="del"),
]