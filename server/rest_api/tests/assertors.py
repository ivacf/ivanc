class ResponseDataAssertor(object):

    required_fields = []
    optional_fields = []
    nested_assertors = []

    @classmethod
    def assertRequiredFields(cls, test_case, data):
        """
        Validate data contains the required fields.
        Also performs the same assertion in any registered nested assertors.
        """
        for field in cls.required_fields:
            test_case.assertIn(field, data)
            test_case.assertIsNotNone(data.get(field), 'Field %s is empty' % (field))

        for (assertor, path) in cls.nested_assertors:
            assertor.assertRequiredFields(test_case, data[path])

    @classmethod
    def assertAllFields(cls, test_case, data):
        """
        Validate data contains all the optional and required fields.
        Also performs the same assertion in any registered nested assertors.
        """
        all_fields = cls.required_fields + cls.optional_fields
        for field in all_fields:
            test_case.assertIn(field, data)
            test_case.assertIsNotNone(data.get(field), 'Field %s is empty' % (field))

        for (assertor, path) in cls.nested_assertors:
            assertor.assertAllFields(test_case, data[path])


class PlatformAssertor(ResponseDataAssertor):
    required_fields = ['name', 'icon', 'url']


class AppAssertor(ResponseDataAssertor):
    required_fields = ['id', 'title', 'url', 'start_date', 'color']
    optional_fields = ['store_url', 'end_date', 'platform', 'image']


class AppAssertorNested(AppAssertor):
    nested_assertors = [(PlatformAssertor, 'platform')]


class RepoAssertor(ResponseDataAssertor):
    required_fields = ['id', 'title', 'subtitle', 'url', 'start_date', 'color']
    optional_fields = ['end_date', 'platform', 'image']


class RepoAssertorNested(RepoAssertor):
    nested_assertors = [(PlatformAssertor, 'platform')]


class ArticleAssertor(ResponseDataAssertor):
    required_fields = ['id', 'title', 'url', 'publish_date', 'color']
    optional_fields = ['platform', 'image']


class ArticleAssertorNested(ArticleAssertor):
    nested_assertors = [(PlatformAssertor, 'platform')]
