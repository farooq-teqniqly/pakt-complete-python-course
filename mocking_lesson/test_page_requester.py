from unittest import TestCase
from unittest.mock import patch
from mocking_lesson.page_requester import PageRequester
from collections import namedtuple


class PageRequesterTests(TestCase):
    def setUp(self):
        self._requester = PageRequester("http://www.github.com")

    def test_get_calls_requests_get(self):
        # Act, Arrange, and Assert
        with patch("requests.get") as mock_get:
            self._requester.get()
            mock_get.assert_called()

    def test_get_returns_text(self):
        # Arrange and Act
        FakeResponse = namedtuple("FakeResponse", ["text"])

        with patch("requests.get", return_value=FakeResponse("Hello")) as mock_get:
            response = self._requester.get()

        # Assert
        self.assertEqual("Hello", response)
