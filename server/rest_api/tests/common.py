import vcr
from rest_api.models import Platform

vcr = vcr.VCR(
    cassette_library_dir='rest_api/tests/fixtures/cassettes',
)


def create_platform(name='Google Play'):
    return Platform.objects.create(
        name=name,
        icon='media/images/platforms/play.svg',
        url='http://play.google.com'
    )
