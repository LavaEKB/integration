from django.urls import path
from .views import MainView, CheckConnectionView, BufferFoodView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('app_label_integr/iiko/', CheckConnectionView.as_view(), name='checkconnection'),
    path('app_label_integr/bufferfood/', BufferFoodView.as_view(), name='bufferfood'),
]

 