from django.urls import path
from .views import MainView, CheckConnectionView, BufferFoodView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('app_label_integr/iiko/', CheckConnectionView.as_view(), name='checkconnection'),
    path('app_label_integr/bufferfood/', BufferFoodView.as_view(), name='bufferfood'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 