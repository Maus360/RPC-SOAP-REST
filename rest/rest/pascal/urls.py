from django.urls import path
from .views import *


urlpatterns = [
    path("class/", ClassViewList.as_view(), name="classes-all"),
    path("class/<int:pk>/", ClassViewDetail.as_view(), name="class"),
    path("type/", TypeViewList.as_view(), name="types-all"),
    path("type/<int:pk>/", TypeViewDetail.as_view(), name="type"),
    path("mathoperation/", MathOperationViewList.as_view(), name="mathoperations-all"),
    path(
        "mathoperation/<int:pk>/",
        MathOperationViewDetail.as_view(),
        name="mathoperation",
    ),
]
