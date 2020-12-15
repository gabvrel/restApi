from rest_framework import serializers, fields
from items.models import Item, ITEM_TYPES
from accounts.serializers import UserSerializer

class ItemSerializer(serializers.ModelSerializer):
    interest = fields.MultipleChoiceField(choices=ITEM_TYPES)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
       