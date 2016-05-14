from urlparse import urlparse
from django.conf import settings
import requests
import requests_cache

# Install an in memory cache for requests so we don't call the github api to retreive the stars
# every time. The cache expires after 12 hours. 
requests_cache.install_cache('requests_cache', backend='memory', expire_after=(12 * 60 * 60))


class InvalidGitHubUrl(Exception):
    pass


class GitHubRepoFetcher(object):

    def fetch(self, repo_url):
        """
        Retrieves data of a GitHub repo using the GitHub rest API given the repo URL
        """
        payload = {
            'client_id': settings.GITHUB['CLIENT_ID'],
            'client_secret': settings.GITHUB['CLIENT_SECRET']
        }
        response = requests.get(self._api_url_from_repo_url(repo_url), params=payload)
        if response.status_code == requests.codes.ok:
            return response.json()
        response.raise_for_status()

    def _api_url_from_repo_url(self, repo_url):
        parts = urlparse(repo_url)
        if parts.netloc != 'github.com' or parts.path is None:
            raise InvalidGitHubUrl()
        return 'https://api.github.com/repos' + parts.path
