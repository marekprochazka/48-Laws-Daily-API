from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LawSerializer, DailyIDSerializer
from .models import Law, DailyId
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from .cron import generate_new_daily_id

class LawsListView(ListAPIView):
    serializer_class = LawSerializer

    def get_queryset(self):
        return Law.objects.all()


class DailyIdView(APIView):
    def get(self,request,format=None):
        daily_id = DailyId.objects.all().first()
        serializer = DailyIDSerializer(daily_id, many=False)
        return Response(serializer.data)


class UpdateDailyId(View):
    def get(self, requst, **kwargs):
        secret_key = kwargs.get('secretkey')
        if secret_key == settings.SECRET_JOB_KEY:
            generate_new_daily_id()
            return  HttpResponse('ok')
        return HttpResponse('not ok')
