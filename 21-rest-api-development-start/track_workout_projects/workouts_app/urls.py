from django.urls import path
from .views import ExerciseAPIView

urlpatterns = [
    path('exercises/', ExerciseAPIView.as_view(), name='exercise-list'),
    path('exercises/<int:id>/', ExerciseAPIView.as_view(), name='exercise-detail')
]