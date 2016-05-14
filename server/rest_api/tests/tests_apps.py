from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_api.models import App
from datetime import datetime
from rest_api.tests.assertors import AppAssertorNested, AppAssertor
from rest_api.tests.common import create_platform


class AppsTests(APITestCase):

    def test_get_apps_when_single_app_saved(self):
        """
        Ensure get apps returns one app with all the expected fields
        """
        create_app()

        url = reverse('apps')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))
        AppAssertorNested.assertAllFields(self, response.data[0])

    def test_get_apps_when_multiple_app_saved(self):
        """
        Ensure get apps returns multiple apps if there is more than one saved
        """
        apps = [
            create_app(title="App 1"),
            create_app(title="App 2"),
            create_app(title="App 3")
        ]

        url = reverse('apps')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(apps), len(response.data))
        for app_response in response.data:
            AppAssertorNested.assertAllFields(self, app_response)

    def test_post_apps_empty_body(self):
        """
        Ensure posting to apps when body is empty returns 400
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        url = reverse('apps')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_apps_non_authenticated_fails(self):
        """
        Check posting apps without authentication return 401
        """
        platform = create_platform()
        data = make_app_data_with_all_fields(platform.id)
        url = reverse('apps')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_app_with_all_fields(self):
        """
        Ensure we can create a new app when sending a body that contains all the possible fields
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        platform = create_platform()
        data = make_app_data_with_all_fields(platform.id)
        url = reverse('apps')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        AppAssertor.assertRequiredFields(self, response.data)

    def test_post_app_with_required_fields(self):
        """
        Ensure we can create a new app when sending a body that contains ONLY the required fields
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        data = make_app_data_with_required_fields()
        url = reverse('apps')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        AppAssertor.assertRequiredFields(self, response.data)

    def test_post_app_with_invalid_color(self):
        """
        Sending an invalid color returns 400
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        data = make_app_data_with_required_fields()
        data['color'] = '#FFCC'
        url = reverse('apps')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# Helper Methods and classes #


def create_app(title='Best app ever', platform=None):
    if not platform:
        platform = create_platform()

    return App.objects.create(
        title=title,
        url='http://ivanc.uk',
        store_url='http://play.google.com',
        start_date=datetime.now(),
        end_date=datetime.now(),
        image='media/images/image.png',
        color='#FFFFFF',
        platform=platform
    )


def make_app_data_with_required_fields():
    return {
        'title': 'Best app ever',
        'url': 'http://ivanc.uk',
        'start_date': '2016-01-15',
        'color': '#FFFFFF'
    }


def make_app_data_with_all_fields(platform_id):
    data = make_app_data_with_required_fields()
    data.update({
        'end_date': '2016-06-15',
        'store_url': 'http://play.google.com/',
        'platform': platform_id
    })
    return data
