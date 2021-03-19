from django.urls import path, include
from .views import Home, process_csv,process_prediction,show_figure

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('process_csv/', process_csv, name='process_csv'),
    path('process_prediction/', process_prediction, name='process_prediction'),
    path('show_figure/',show_figure, name='show_figure'),
]
