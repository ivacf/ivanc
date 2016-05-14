from django.test import TestCase
from rest_api.helpers import GitHubRepoFetcher, InvalidGitHubUrl
from rest_api.tests.common import vcr


class GitHubRepoFetcherTests(TestCase):

    def test_fetch_malform_url(self):
        """
        Fetch a repo with a malformed url raises InvalidGitHubUrl exception
        """
        url = 'http://githubcom'
        with self.assertRaises(InvalidGitHubUrl):
            GitHubRepoFetcher().fetch(url)

    def test_fetch_non_github_repo(self):
        """
        Fetch a non GitHub repo raises InvalidGitHubUrl exception
        """
        url = 'http://gitlab.com/ivacf/archi'
        with self.assertRaises(InvalidGitHubUrl):
            GitHubRepoFetcher().fetch(url)

    @vcr.use_cassette()
    def test_fetch_invalid_github_repo(self):
        """
        Fetch a GitHub url that is not a valid repo raises an Exception
        """
        url = 'https://github.com/archi'
        with self.assertRaises(Exception):
            GitHubRepoFetcher().fetch(url)

    @vcr.use_cassette()
    def test_fetch_valid_github_repo(self):
        """
        Ensure we can fetch a valid GitHub repos
        """
        url = 'https://github.com/ivacf/archi'
        repo = GitHubRepoFetcher().fetch(url)
        self.assertEqual('archi', repo['name'])
