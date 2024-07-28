from django.urls import path
from djangoproject.phonebook.views import landing_page, create_contact

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('new-conttact', create_contact, name='new-contact')
]