
from django.urls import path
from .views import *

urlpatterns = [
    path('api/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('api/view_cart/', view_cart, name='view_cart'),
    path('api/delete_cart/', delete_cart, name='delete_cart'),
    path('show-session-id/', show_session_id, name='show_session_id'),

]
