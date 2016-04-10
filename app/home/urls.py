from django.conf.urls import url

from home.views import LandingView


urlpatterns = [
    url(r'^', LandingView.as_view(), name='home.landing'),
]
