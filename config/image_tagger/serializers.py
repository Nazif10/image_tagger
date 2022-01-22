from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from image_tagger.models import Image


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    submitter = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Image
        fields = ("title", "creation_date", "submitter", "image", "tags", "id")
