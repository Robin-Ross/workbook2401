from django.urls import path
from .views import AnnoucementListView, CreateAnnouncementView

urlpatterns = [
    path('', AnnoucementListView.as_view(), name='announcement_list'),
    path('create/', CreateAnnouncementView.as_view(), name='create_announcement'),
]
