from items.models import Item
from django.db.models import F
from rest_framework import generics, filters
from items.serializers import ItemSerializer


class PublicItemsViewSet(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.OrderingFilter]

"""     def get_queryset(self):
        lat = self.request.query_params.get('lat', None)
        lgn = self.request.query_params.get('lng', None) """



class ItemFilterViewSet(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        itemType = self.kwargs['itemType']
        return Item.objects.filter(itemType=itemType)


class ItemSearchViewSet(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class UserItemSerializer(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        userId = self.request.query_params.get('userId', None)
        queryset = (Item.objects.all())
        if userId is not None:
            return queryset.filter(user=userId)
        return []
