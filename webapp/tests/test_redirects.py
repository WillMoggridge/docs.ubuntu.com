from django.test import SimpleTestCase


class RedirectTestCase(SimpleTestCase):
    def _assertRedirect(self, requested, expected):
        self.assertRedirects(
            self.client.get(requested),
            expected,
            fetch_redirect_response=False,
        )

    def _assertDoesNotRedirect(self, requested):
        response = self.client.get(requested)
        self.assertTrue(response.status_code not in [301, 302])


class RedirectCoreTestCase(RedirectTestCase):
    home = '/core/en/'
    test_page = '/core/en/test'
    test_index = '/core/en/test/index'

    def test_redirect_core_to_en(self):
        self._assertRedirect('/core', self.home)
        self._assertRedirect('/core/', self.home)
        self._assertRedirect('/core/en', self.home)
        self._assertDoesNotRedirect(self.home)

    def test_does_not_redirect_maas_simple_path(self):
        self._assertDoesNotRedirect(self.test_page)
        self._assertDoesNotRedirect(self.test_index)

    def test_redirect_core_simple_path(self):
        self._assertRedirect('/core/en/test/', self.test_page)
        self._assertRedirect('/core/en/test/index.html', self.test_index)


class RedirectPhoneTestCase(RedirectTestCase):
    home = '/phone/en/'
    test_page = '/phone/en/test'
    test_index = '/phone/en/test/index'

    def test_redirect_phone_to_en(self):
        self._assertRedirect('/phone', self.home)
        self._assertRedirect('/phone/', self.home)
        self._assertRedirect('/phone/en', self.home)
        self._assertDoesNotRedirect(self.home)

    def test_redirect_phone_simple_path(self):
        self._assertRedirect('/phone/en/test/', self.test_page)
        self._assertRedirect('/phone/en/test/index.html', self.test_index)


class RedirectMAASTestCase(RedirectTestCase):
    home = '/maas/2.1/en/'
    test_page = '/maas/2.1/en/test'
    test_index = '/maas/2.1/en/test/index'

    def test_does_not_redirect_maas_root_path(self):
        self._assertDoesNotRedirect(self.home)

    def test_redirect_maas_to_en_with_version(self):
        self._assertRedirect('/maas', self.home)
        self._assertRedirect('/maas/', self.home)
        self._assertRedirect('/maas/2.1', self.home)
        self._assertRedirect('/maas/2.1/', self.home)
        self._assertRedirect('/maas/2.1/en', self.home)
        self._assertRedirect('/maas/en', self.home)
        self._assertRedirect('/maas/en/', self.home)

    def test_does_not_redirect_maas_simple_path(self):
        self._assertDoesNotRedirect(self.test_page)
        self._assertDoesNotRedirect(self.test_index)

    def test_redirect_maas_simple_path(self):
        self._assertRedirect('/maas/2.1/en/test/', self.test_page)
        self._assertRedirect('/maas/2.1/en/test/index.html', self.test_index)
