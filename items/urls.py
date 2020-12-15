from django.urls import path
from items.api import PublicItemsViewSet, ItemFilterViewSet, ItemSearchViewSet, UserItemSerializer

urlpatterns = [
    path('public', PublicItemsViewSet.as_view()),
    path('searchItem', ItemSearchViewSet.as_view()),
    path('userItems', UserItemSerializer.as_view()),
    path('itemsFilter/<itemType>/', ItemFilterViewSet.as_view()),
]
