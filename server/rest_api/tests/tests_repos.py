from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_api.models import Repo
from datetime import datetime
from rest_api.tests.assertors import RepoAssertorNested, RepoAssertor
from rest_api.tests.common import vcr, create_platform


class RepoTests(APITestCase):

    @vcr.use_cassette()
    def test_get_repos_when_single_repo_saved(self):
        """
        Ensure get repos returns one repo with all the expected fields
        """
        create_repo()

        url = reverse('repos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))
        RepoAssertorNested.assertAllFields(self, response.data[0])

    @vcr.use_cassette()
    def test_get_repos_when_multiple_repos_saved(self):
        """
        Ensure get repos returns multiple repos if there is more than one saved
        """
        repos = [
            create_repo(title="Repo 1"),
            create_repo(title="Repo 2"),
            create_repo(title="Repo 3"),
        ]

        url = reverse('repos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(repos), len(response.data))
        for app_response in response.data:
            RepoAssertorNested.assertAllFields(self, app_response)

    def test_post_repos_empty_body(self):
        """
        Ensure posting to repos when body is empty returns 400
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        url = reverse('repos')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_repos_non_authenticated_fails(self):
        """
        Check posting to repos without authentication return 401
        """
        platform = create_platform()
        data = make_repo_data_with_all_fields(platform.id)
        url = reverse('repos')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_repo_with_all_fields(self):
        """
        Ensure we can create a new repo when sending a body that contains all the possible fields
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        platform = create_platform()
        data = make_repo_data_with_all_fields(platform.id)
        url = reverse('repos')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        RepoAssertor.assertRequiredFields(self, response.data)

    def test_post_repo_with_required_fields(self):
        """
        Ensure we can create a new repo when sending a body that contains ONLY the required fields
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        data = make_repo_data_with_required_fields()
        url = reverse('repos')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        RepoAssertor.assertRequiredFields(self, response.data)

    def test_post_repo_with_invalid_color(self):
        """
        Sending an invalid color returns 400
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        data = make_repo_data_with_required_fields()
        data['color'] = '#FFCC'
        url = reverse('repos')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Helper Methods and classes #

def create_repo(title='Best repo ever', platform=None):
    if not platform:
        platform = create_platform()

    return Repo.objects.create(
        title=title,
        subtitle='Subtitle',
        url='https://github.com/ivacf/archi',
        start_date=datetime.now(),
        end_date=datetime.now(),
        image='media/images/image.png',
        color='#FFFFFF',
        platform=platform
    )


def make_repo_data_with_required_fields():
    return {
        'title': 'Repo title',
        'subtitle': 'Repo subtitle',
        'url': 'http://ivanc.uk',
        'start_date': '2016-01-15',
        'color': '#FFFFFF'
    }


def make_repo_data_with_all_fields(platform_id):
    data = make_repo_data_with_required_fields()
    data.update({
        'end_date': '2016-06-15',
        'platform': platform_id
    })
    return data
