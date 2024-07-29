from django.urls import path
from .views import CardCreateView, CardsBatchCreateView, CardRetrieveByNumberView

urlpatterns = [
    path("add/", CardCreateView.as_view(), name="add_card"),
    path("batch/", CardsBatchCreateView.as_view(), name="add_batch"),
    path(
        "get_by_number/<str:card_number>/",
        CardRetrieveByNumberView.as_view(),
        name="get_card_by_number",
    ),
]
