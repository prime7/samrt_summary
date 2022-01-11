from django.urls import path
from api.views import SummaryAPIView,SummaryReviewAPIView


urlpatterns = [
    path('summary/',SummaryAPIView.as_view(),name='summary'),
    path('summary/rate/',SummaryReviewAPIView.as_view(),name='summary-review')
]