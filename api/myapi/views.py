from rest_framework.generics import ListAPIView
from .serializers import LawSerializer
from .models import Law


class LawsListView(ListAPIView):
    serializer_class = LawSerializer

    def get_queryset(self):
        return Law.objects.all()
