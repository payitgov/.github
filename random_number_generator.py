#!/usr/bin/env python3
"""
Random Number Generator
Generates a random number between 1 and 100 (inclusive)
"""

import random

def generate_random_number(min_val=1, max_val=100):
    """
    Generate a random number between min_val and max_val (inclusive)
    
    Args:
        min_val (int): Minimum value (default: 1)
        max_val (int): Maximum value (default: 100)
    
    Returns:
        int: Random number between min_val and max_val
    """
    return random.randint(min_val, max_val)

def main():
    """Main function to demonstrate random number generation"""
    print("Random Number Generator")
    print("=" * 25)
    
    # Generate a single random number
    random_num = generate_random_number()
    print(f"Random number between 1 and 100: {random_num}")
    
    # Generate multiple random numbers
    print("\nGenerating 5 random numbers:")
    for i in range(5):
        num = generate_random_number()
        print(f"  {i+1}. {num}")
    
    # Custom range example
    print("\nCustom range (1-10):")
    for i in range(3):
        num = generate_random_number(1, 10)
        print(f"  {i+1}. {num}")

if __name__ == "__main__":
    main()