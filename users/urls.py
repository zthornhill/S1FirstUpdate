from django.urls import path
#from . import views
from .views import SignUpView
from .views import aboutView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', aboutView.as_view(), name='about')
]
