import random

def random_vowel():
    return random.choice('aeiou')

def random_consonant():
    return random.choice('bcdfghjklmnpqrstvwxyz')

def generate_fantasy_name(base_name):
    name_parts = [
        random_consonant(),
        random_vowel(),
        random_consonant(),
        random_vowel()
    ]
    random_suffix = ''.join(random.choices(["ar", "ian", "iel", "ath", "ius"], k=1))
    return base_name.capitalize() + ''.join(name_parts) + random_suffix

def main():
    print("Welcome to the Fantasy Name Generator!")
    base_name = input("Enter a base name to build off of (e.g., your pet's name): ").strip()
    if not base_name:
        print("You didn't enter a name. No fantasy for you!")
        return
    
    fantasy_name = generate_fantasy_name(base_name)
    print(f"Behold! Your epic fantasy name is: {fantasy_name}")

if __name__ == "__main__":
    main()
