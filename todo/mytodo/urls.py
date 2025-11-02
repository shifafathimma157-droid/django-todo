from django.urls import path
from . import views

urlpatterns=[
    path("addtask/",views.AddTaskView,name='addtask'),
    path('markdone<int:pk>/',views.MarkDone,name="markdone"),
    path('markundone<int:pk>/',views.MarkUnDone,name="markundone"),
    path('edittask<int:pk>/',views.EditTask,name="edittask"),
    path('delettask<int:pk>/',views.DeleteTask,name="deltask"),


]