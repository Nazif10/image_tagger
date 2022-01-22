from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from image_tagger.models import Image
from image_tagger.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Image.objects.all().order_by("creation_date")
    filter_backends = [filters.SearchFilter]
    search_fields = ["tags__name"]
    serializer_class = ImageSerializer

    def get_serializer_context(self):
        context = super(ImageViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
