from django.urls import path

from . import views

urlpatterns=[
    path("",views.index),
    path("create",views.create),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete)

    # path("",views.index),
    # path("",views.create),
    # path('<int:id>', views.edit),
    # path('<int:id>', views.delete)
]