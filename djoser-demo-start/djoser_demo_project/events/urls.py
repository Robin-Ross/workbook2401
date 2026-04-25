from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventAPIView, TalkViewSet

# TODO Part 2: Import EventAPIView and add URL patterns:
#   - events/          → EventAPIView (name: event-list-create)
#   - events/<int:pk>/ → EventAPIView (name: event-detail)

# TODO Part 3: Import TalkViewSet, create a DefaultRouter,
#   register TalkViewSet with prefix "talks", and include router.urls
router = DefaultRouter()
router.register(r"talks", TalkViewSet, basename="talk")

urlpatterns = [
    # URL patterns go here
    path("events/", EventAPIView.as_view(), name="event-list-create"),
    path("events/<int:pk>/", EventAPIView.as_view(), name="event-detail"),
    path("", include(router.urls)),
]
