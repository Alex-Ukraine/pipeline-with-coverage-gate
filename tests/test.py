from unittest import TestCase
from main import get_sum


class GetSumTestCase(TestCase):
    def test_get_sum(self) -> None:
        result = get_sum(12, 13)
        assert result == 25
