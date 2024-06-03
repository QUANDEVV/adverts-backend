from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework.decorators import api_view

from .models import Banner
from .serializers import BannerSerializer
from django.utils import timezone

# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")


@api_view(['GET'])
def banners_list(request):
    """
    Retrieve list of banners.
    """
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get_queryset(self):
        # Filter out expired bookings
        now = timezone.now()
        return Banner.objects.filter(is_booked=False) | Banner.objects.filter(is_booked=True, booking_end__gt=now)

    @action(detail=False, methods=['get'])
    def active(self, request):
        now = timezone.now()
        active_banners = Banner.objects.filter(is_booked=True, booking_end__gt=now)
        serializer = self.get_serializer(active_banners, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def empty(self, request):
        empty_slots = Banner.objects.filter(is_booked=False)
        serializer = self.get_serializer(empty_slots, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        duration = int(data['duration'])
        price = float(data['price'])

        booking_start = timezone.now()
        booking_end = booking_start + timezone.timedelta(days=duration)

        banner = Banner(
            avatar_image=data['avatar_image'],
            ig_link=data['ig_link'],
            onlyfans_link=data['onlyfans_link'],
            price=price,
            duration=timezone.timedelta(days=duration),
            is_booked=True,
            booking_start=booking_start,
            booking_end=booking_end,
            slot_number=data['slot_number'],
        )
        banner.save()

        serializer = self.get_serializer(banner)
        return Response(serializer.data)
