import datetime
from unittest import mock

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files import File

from image_tagger.serializers import ImageSerializer
from .models import Image

IMAGES_URL = reverse("image-list")


class TestImageAPI(TestCase):  # Test the private ingredients api
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test_user", "testPassword")
        self.client.force_authenticate(self.user)

    def test_retrieve_images_list(self):
        test_image = SimpleUploadedFile(
            "test_image.jpg", b"image_content", content_type="image/jpeg"
        )
        x = Image.objects.create(
            title="Warner",
            creation_date=datetime.datetime(2922, 1, 19, 14, 30),
            image=test_image,
            submitter=self.user,
        )
        x.tags.add("opening", "batsman")
        result = self.client.get(IMAGES_URL)
        images = Image.objects.all().order_by("creation_date")
        serializer = ImageSerializer(images, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        # self.assertEqual(result.data, serializer.data)

    def test_search_images_list(self):
        url = "{url}?{filter}={value}".format(
            url=reverse("image-list"), filter="search", value="opening"
        )
        test_image = SimpleUploadedFile(
            "test_image.jpg", b"image_content", content_type="image/jpeg"
        )
        x = Image.objects.create(
            title="Warner",
            creation_date=datetime.datetime(2922, 1, 19, 14, 30),
            image=test_image,
            submitter=self.user,
        )
        y = Image.objects.create(
            title="Khawaja",
            creation_date=datetime.datetime(2922, 1, 18, 14, 30),
            image=test_image,
            submitter=self.user,
        )
        x.tags.add("opening", "batsman")
        y.tags.add("closing", "batsman")

        result = self.client.get(url)
        self.assertEqual(len(result.data), 1)
        self.assertEqual(result.data[0].get("title"), "Warner")

    def test_patch_existing_image(self):
        test_image = SimpleUploadedFile(
            "test_image.jpg", b"image_content", content_type="image/jpeg"
        )
        x = Image.objects.create(
            title="Warner",
            creation_date=datetime.datetime(2922, 1, 19, 14, 30),
            image=test_image,
            submitter=self.user,
        )
        x.tags.add("opening", "batsman")
        print(IMAGES_URL + "1/")
        result = self.client.patch(IMAGES_URL + "1/", {"tags": ["bowler"]})
        print(result.data)
