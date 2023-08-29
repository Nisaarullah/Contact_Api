from django.urls import path
from .views import submit_contact_form

urlpatterns = [
    path('submit-contact-form/', submit_contact_form, name='submit_contact_form'),
]
