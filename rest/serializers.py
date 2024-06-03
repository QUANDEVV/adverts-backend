from rest_framework import serializers
# from.models import Beach
# from.models import Video
from.models import Banner
from cloudinary.uploader import upload








class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'




