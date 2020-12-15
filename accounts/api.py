from rest_framework import generics, serializers, permissions
from accounts.serializers import UserSerializer, LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from accounts.models import User

class UserApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,
                context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })

class UserAuthApi(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user,
                                       context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })