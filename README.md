# Birthday Wishes Generator 🎉

A simple Python application to generate personalized birthday wishes with various options including random wishes, personalized messages, funny wishes, and birthday countdowns.

## Features

- **Random Birthday Wishes**: Get a random birthday wish
- **Personalized Wishes**: Generate custom wishes with the person's name and age
- **Funny Wishes**: Get humorous birthday messages
- **Birthday Countdown**: Calculate days until a birthday

## Installation

No external dependencies required! Just Python 3.x

```bash
git clone https://github.com/aliyanmansoor96-hub/Birthday-wishes.git
cd Birthday-wishes
```

## Usage

### Run the Script

```bash
python birthday_wishes.py
```

### Use as a Module

```python
from birthday_wishes import BirthdayWishes

# Get a random wish
wish = BirthdayWishes.get_random_wish()
print(wish)

# Get a personalized wish
personalized = BirthdayWishes.get_personalized_wish("Alice", 25)
print(personalized)

# Get a funny wish
funny = BirthdayWishes.get_funny_wish()
print(funny)

# Calculate birthday countdown
days_left = BirthdayWishes.birthday_countdown("2026-08-15")
print(f"Days until birthday: {days_left}")
```

## Methods

### `get_random_wish()`
Returns a random birthday wish from the predefined list.

### `get_personalized_wish(name, age=None)`
Generates a personalized birthday wish with the person's name and optional age.

**Parameters:**
- `name` (str): Person's name
- `age` (int, optional): Person's age

### `get_funny_wish()`
Returns a funny/humorous birthday wish.

### `birthday_countdown(target_date)`
Calculates the number of days until a birthday.

**Parameters:**
- `target_date` (str): Date in format "YYYY-MM-DD"

**Returns:**
- `int`: Number of days until the birthday

## Example Output

```
🎉 Birthday Wishes Generator 🎉

Random Birthday Wish:
Happy Birthday! Wishing you a day filled with joy and happiness!

Personalized Birthday Wish:
Happy Birthday, Alice! May your special day be as amazing as you are!
🎂 You're turning 25 today!

Funny Birthday Wish:
You're not old, you're retro!

Birthday Countdown:
Days until next birthday: 45 days
```

## Contributing

Feel free to fork this repository and submit pull requests with additional wishes or features!

## License

This project is open source and available for anyone to use and modify.

## Author

Created by aliyanmansoor96-hub

---

**Enjoy spreading birthday cheer! 🎂🎈**
