from django.urls import path
from .views import Services, SubmissionForm

urlpatterns = [
    path('save-services/<int:id>/', Services.as_view(), name='services'),
    # path('fetch-specific-new-car/<int:id>/', Services.as_view(), name='services'),
    path('submission-form/', SubmissionForm.as_view(), name='submission-form'),

]
