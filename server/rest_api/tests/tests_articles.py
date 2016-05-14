from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_api.models import Article
from datetime import datetime
from rest_api.tests.assertors import ArticleAssertorNested, ArticleAssertor
from rest_api.tests.common import create_platform


class ArticlesTests(APITestCase):

    def test_get_articles_when_single_article_saved(self):
        """
        Ensure get articles returns one article with all the expected fields
        """
        create_article()

        url = reverse('articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))
        ArticleAssertorNested.assertAllFields(self, response.data[0])

    def test_get_article_when_multiple_articles_saved(self):
        """
        Ensure get articles returns multiple articles if there are more than one saved
        """
        articles = [
            create_article(title="Article 1"),
            create_article(title="Article 2"),
            create_article(title="Article 3")
        ]

        url = reverse('articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(articles), len(response.data))
        for article_response in response.data:
            ArticleAssertorNested.assertAllFields(self, article_response)

    def test_post_articles_empty_body(self):
        """
        Ensure posting to articles when body is empty returns 400
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        url = reverse('articles')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_articles_non_authenticated_fails(self):
        """
        Check posting articles without authentication return 401
        """
        platform = create_platform()
        data = make_article_data_with_all_fields(platform.id)
        url = reverse('articles')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_article_with_all_fields(self):
        """
        Ensure we can create a new article when sending a body that contains all the possible fields
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        platform = create_platform()
        data = make_article_data_with_all_fields(platform.id)
        url = reverse('articles')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        ArticleAssertor.assertRequiredFields(self, response.data)

    def test_post_article_with_required_fields(self):
        """
        We can create a new article when sending a body that contains ONLY the required fields
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        data = make_article_data_with_required_fields()
        url = reverse('articles')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        ArticleAssertor.assertRequiredFields(self, response.data)

    def test_post_article_with_invalid_color(self):
        """
        Sending an invalid color returns 400
        """
        user = User.objects.create(username='ivan')
        self.client.force_authenticate(user=user)

        data = make_article_data_with_required_fields()
        data['color'] = '#FFCC'
        url = reverse('articles')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# Helper Methods and classes #


def create_article(title='Best article ever', platform=None):
    if not platform:
        platform = create_platform()

    return Article.objects.create(
        title=title,
        url='http://ivanc.uk',
        publish_date=datetime.now(),
        image='media/images/image.png',
        color='#FFFFFF',
        platform=platform
    )


def make_article_data_with_required_fields():
    return {
        'title': 'Best article ever',
        'url': 'http://ivanc.uk',
        'publish_date': '2016-01-15',
        'color': '#FFFFFF'
    }


def make_article_data_with_all_fields(platform_id):
    data = make_article_data_with_required_fields()
    data.update({
        'platform': platform_id
    })
    return data
