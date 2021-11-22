
from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('success/', SuccessView.as_view()),
    path('cancelled/', CancelledView.as_view()),
    path('webhook/', stripe_webhook),
    path('home/', HomePage.as_view()),
]