from django.urls import path, include
from .views import (
    Home, process_csv, process_prediction1, graph2, graph1,
    process_csv_display1, graph1, process_csv_display2, process_csv_display3
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('process_csv/', process_csv, name='process_csv'),
    path('process_prediction1/', process_prediction1, name='process_prediction1'),
    path('process_prediction2/', process_prediction1, name='process_prediction2'),
    # path('show_figure/',show_figure, name='show_figure'),
    path('graph1/', graph1, name='graph1'),
    path('graph2/', graph2, name='graph2'),
    path('process_csv_display1/', process_csv_display1,
         name='process_csv_display1'),
    path('process_csv_display2/', process_csv_display2,
         name='process_csv_display2'),
    path('process_csv_display3/', process_csv_display3,
         name='process_csv_display3'),
]
