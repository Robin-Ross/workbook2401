from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOrganizer
from .models import Event, Talk
from .serializers import EventSerializer, TalkSerializer

# TODO Part 2: Create EventAPIView extending APIView
#   - get(self, request, pk=None): return single event by pk, or all events
#   - post(self, request): create a new event (organizer only)
#   - get_permissions(self): return [IsOrganizer()] for POST, [IsAuthenticated()] otherwise
class EventAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsOrganizer()]
        return [IsAuthenticated()]

    def get(self, request, pk=None):
        if pk:
            try:
                event = Event.objects.get(pk=pk)
            except Event.DoesNotExist:
                return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)

        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Part 3: Create TalkViewSet extending viewsets.ModelViewSet
#   - queryset: all Talk objects
#   - serializer_class: TalkSerializer
#   - permission_classes: (IsAuthenticated,)
class TalkViewSet(viewsets.ModelViewSet):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
    permission_classes = [IsAuthenticated]