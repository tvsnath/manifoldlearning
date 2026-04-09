from hello import add, subtract, get_weather


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-4, -6) == -10

    def test_add_mixed_signs(self):
        assert add(-1, 5) == 4

    def test_add_zeros(self):
        assert add(0, 0) == 0

    def test_add_with_zero(self):
        assert add(7, 0) == 7


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative_numbers(self):
        assert subtract(-4, -2) == -2

    def test_subtract_mixed_signs(self):
        assert subtract(5, -3) == 8

    def test_subtract_zeros(self):
        assert subtract(0, 0) == 0

    def test_subtract_same_numbers(self):
        assert subtract(9, 9) == 0


class TestGetWeather:
    def test_returns_string(self):
        result = get_weather.invoke("London")
        assert isinstance(result, str)

    def test_contains_location(self):
        result = get_weather.invoke("Paris")
        assert "Paris" in result

    def test_different_location(self):
        result = get_weather.invoke("Tokyo")
        assert "Tokyo" in result
