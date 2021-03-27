from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LawSerializer, DailyIDSerializer
from .models import Law, DailyId


class LawsListView(ListAPIView):
    serializer_class = LawSerializer

    def get_queryset(self):
        return Law.objects.all()


class DailyIdView(APIView):
    def get(self,request,format=None):
        daily_id = DailyId.objects.all().first()
        serializer = DailyIDSerializer(daily_id, many=False)
        return Response(serializer.data)
