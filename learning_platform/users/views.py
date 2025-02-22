from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionView(APIView):
    def post(self, request):
        user = request.user
        amount = 100 * 100

        paystack_url = f"https://paystack.com/pay/{user.id}"

        subscription, created = Subscription.objects.get_or_create(user=user)
        subscription.is_active = True
        subscription.expires_at = now() + timedelta(days=7)
        subscription.save()

        return Response({"message": "Subscription successful", "paystack_url": paystack_url})
