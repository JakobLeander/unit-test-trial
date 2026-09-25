class PracticeHelpers:
    """Small helper methods for practicing unit testing."""

    def add_numbers(self, first: float, second: float) -> float:
        return first + second

    def is_even(self, number: int) -> bool:
        return number % 2 == 0

    def reverse_text(self, text: str) -> str:
        return text[::-1]

    def count_vowels(self, text: str) -> int:
        return sum(character.lower() in "aeiou" for character in text)

    def factorial(self, number: int) -> int:
        if number < 0:
            raise ValueError("factorial is undefined for negative numbers")

        result = 1
        for value in range(2, number + 1):
            result *= value
        return result

    def find_maximum(self, numbers: list[float]) -> float:
        if not numbers:
            raise ValueError("numbers must not be empty")
        return max(numbers)

    def remove_duplicates(self, values: list[str]) -> list[str]:
        return list(dict.fromkeys(values))

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9 / 5) + 32

    def is_palindrome(self, text: str) -> bool:
        normalized = "".join(character.lower() for character in text if character.isalnum())
        return normalized == normalized[::-1]

    def word_frequency(self, text: str) -> dict[str, int]:
        frequency: dict[str, int] = {}
        for word in text.lower().split():
            frequency[word] = frequency.get(word, 0) + 1
        return frequency

    def is_prime(self, number: int) -> bool:
        if number < 2:
            return False
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                return False
        return True

    def calculate_average(self, numbers: list[float]) -> float:
        if not numbers:
            raise ValueError("numbers must not be empty")
        return sum(numbers) / len(numbers)

    def clamp(self, value: float, minimum: float, maximum: float) -> float:
        if minimum > maximum:
            raise ValueError("minimum must not be greater than maximum")
        return max(minimum, min(value, maximum))