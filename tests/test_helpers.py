import pytest

from helpers import PracticeHelpers


@pytest.fixture
def helpers() -> PracticeHelpers:
    return PracticeHelpers()


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [(2, 3, 5), (-1.5, 2.5, 1.0)],
)
def test_add_numbers(helpers, first, second, expected):
    assert helpers.add_numbers(first, second) == expected


@pytest.mark.parametrize("number, expected", [(2, True), (7, False), (0, True)])
def test_is_even(helpers, number, expected):
    assert helpers.is_even(number) is expected


def test_reverse_text(helpers):
    assert helpers.reverse_text("python") == "nohtyp"


def test_count_vowels_is_case_insensitive(helpers):
    assert helpers.count_vowels("Unit Testing") == 4


@pytest.mark.parametrize("number, expected", [(0, 1), (1, 1), (5, 120)])
def test_factorial(helpers, number, expected):
    assert helpers.factorial(number) == expected


def test_factorial_rejects_negative_numbers(helpers):
    with pytest.raises(ValueError, match="negative"):
        helpers.factorial(-1)


def test_find_maximum(helpers):
    assert helpers.find_maximum([-3, 8, 2]) == 8


def test_find_maximum_rejects_empty_lists(helpers):
    with pytest.raises(ValueError, match="empty"):
        helpers.find_maximum([])


def test_remove_duplicates_preserves_order(helpers):
    assert helpers.remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_celsius_to_fahrenheit(helpers):
    assert helpers.celsius_to_fahrenheit(100) == pytest.approx(212)


@pytest.mark.parametrize(
    "text, expected",
    [("A man, a plan, a canal: Panama!", True), ("unit test", False)],
)
def test_is_palindrome(helpers, text, expected):
    assert helpers.is_palindrome(text) is expected


def test_word_frequency_is_case_insensitive(helpers):
    assert helpers.word_frequency("Test test code") == {"test": 2, "code": 1}


@pytest.mark.parametrize("number, expected", [(1, False), (2, True), (13, True), (15, False)])
def test_is_prime(helpers, number, expected):
    assert helpers.is_prime(number) is expected


def test_calculate_average(helpers):
    assert helpers.calculate_average([2, 4, 8]) == pytest.approx(14 / 3)


def test_calculate_average_rejects_empty_lists(helpers):
    with pytest.raises(ValueError, match="empty"):
        helpers.calculate_average([])


@pytest.mark.parametrize(
    ("value", "minimum", "maximum", "expected"),
    [(-1, 0, 10, 0), (5, 0, 10, 5), (12, 0, 10, 10)],
)
def test_clamp(helpers, value, minimum, maximum, expected):
    assert helpers.clamp(value, minimum, maximum) == expected


def test_clamp_rejects_reversed_bounds(helpers):
    with pytest.raises(ValueError, match="maximum"):
        helpers.clamp(5, 10, 0)


@pytest.mark.parametrize(
    "count, expected",
    [(0, []), (1, [0]), (5, [0, 1, 1, 2, 3])],
)
def test_fibonacci(helpers, count, expected):
    assert helpers.fibonacci(count) == expected


def test_fibonacci_rejects_negative_counts(helpers):
    with pytest.raises(ValueError, match="negative"):
        helpers.fibonacci(-1)


@pytest.mark.parametrize(
    "first, second, expected",
    [("listen", "silent", True), ("Dormitory", "dirty room", True), ("python", "pytest", False)],
)
def test_is_anagram(helpers, first, second, expected):
    assert helpers.is_anagram(first, second) is expected


@pytest.mark.parametrize("text, expected", [("one two three", 3), ("", 0), ("  one   two  ", 2)])
def test_count_words(helpers, text, expected):
    assert helpers.count_words(text) == expected


def test_calculate_percentage(helpers):
    assert helpers.calculate_percentage(25, 200) == pytest.approx(12.5)


def test_calculate_percentage_rejects_zero_total(helpers):
    with pytest.raises(ValueError, match="zero"):
        helpers.calculate_percentage(1, 0)


@pytest.mark.parametrize(
    "values, positions, expected",
    [([], 2, []), (["a", "b", "c"], 0, ["a", "b", "c"]), (["a", "b", "c"], 1, ["c", "a", "b"]), (["a", "b", "c"], -1, ["b", "c", "a"])],
)
def test_rotate_list(helpers, values, positions, expected):
    assert helpers.rotate_list(values, positions) == expected
