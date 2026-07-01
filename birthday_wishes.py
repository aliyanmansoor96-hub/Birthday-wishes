#!/usr/bin/env python3
"""
Birthday Wishes Generator
A simple application to generate personalized birthday wishes
"""

import random
from datetime import datetime


class BirthdayWishes:
    """Generate personalized birthday wishes"""
    
    wishes = [
        "Happy Birthday! Wishing you a day filled with joy and happiness!",
        "May your special day be as amazing as you are!",
        "Here's to another year of laughter, love, and adventures!",
        "Wishing you a birthday that's as bright and beautiful as you!",
        "Another year older, another year wiser! Happy Birthday!",
        "May all your dreams come true on your special day!",
        "Happy Birthday! You deserve all the happiness in the world!",
        "Cheers to you on your birthday! Here's to making more memories!",
        "Wishing you a year filled with success, health, and happiness!",
        "Happy Birthday to someone truly special!",
    ]
    
    @staticmethod
    def get_random_wish():
        """Return a random birthday wish"""
        return random.choice(BirthdayWishes.wishes)
    
    @staticmethod
    def get_personalized_wish(name, age=None):
        """Generate a personalized birthday wish"""
        wish = BirthdayWishes.get_random_wish()
        personalized = f"Happy Birthday, {name}! " + wish
        
        if age:
            personalized += f"\n🎂 You're turning {age} today!"
        
        return personalized
    
    @staticmethod
    def get_funny_wish():
        """Return a funny birthday wish"""
        funny_wishes = [
            "Congratulations! You're one year closer to getting senior discounts!",
            "You're not old, you're retro!",
            "Don't worry about your age, you'll get used to it!",
            "You're now officially one year closer to your next birthday!",
            "Age is just a number... and in your case, a BIG number! 😄",
        ]
        return random.choice(funny_wishes)
    
    @staticmethod
    def birthday_countdown(target_date):
        """Calculate days until birthday"""
        today = datetime.now().date()
        target = datetime.strptime(target_date, "%Y-%m-%d").date()
        
        # If birthday already passed this year, calculate for next year
        if target < today:
            target = target.replace(year=target.year + 1)
        
        days_left = (target - today).days
        return days_left


def main():
    """Main function to demonstrate birthday wishes"""
    print("🎉 Birthday Wishes Generator 🎉\n")
    
    # Example 1: Random wish
    print("Random Birthday Wish:")
    print(BirthdayWishes.get_random_wish())
    print()
    
    # Example 2: Personalized wish
    print("Personalized Birthday Wish:")
    personalized = BirthdayWishes.get_personalized_wish("Alice", 25)
    print(personalized)
    print()
    
    # Example 3: Funny wish
    print("Funny Birthday Wish:")
    print(BirthdayWishes.get_funny_wish())
    print()
    
    # Example 4: Birthday countdown
    print("Birthday Countdown:")
    countdown = BirthdayWishes.birthday_countdown("2026-08-15")
    print(f"Days until next birthday: {countdown} days")


if __name__ == "__main__":
    main()
