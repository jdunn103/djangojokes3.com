from django.urls import path

from .views import JobAppView, JobAppThanksView

urlpatterns = [
    path('job-app/', JobAppView.as_view(), name='job-app'),
    path('job-app/thanks/', JobAppThanksView.as_view(), name='job-app-thanks'),
]