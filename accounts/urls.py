from django.urls import path

from . import views
from . views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("me/", views.index, name="me"),
    path("me/reviews/<int:review_id>", views.review, name="review"),
]