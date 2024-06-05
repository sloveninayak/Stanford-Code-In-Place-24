import random

def generate_password(length, uppercase, lowercase, numbers, symbols):
  char_sets = []
  if uppercase:
    char_sets.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  if lowercase:
    char_sets.append("abcdefghijklmnopqrstuvwxyz")
  if numbers:
    char_sets.append("0123456789")
  if symbols:
    char_sets.append("!@#$%^&*()_-+={}|[]\:;'<,>.?/`")

  # Ensure at least one character set is selected
  if not char_sets:
    raise ValueError("Please select at least one character type.")

  # Combine character sets and shuffle them for randomness
  all_chars = "".join(char_sets)
  all_chars_list = list(all_chars)
  random.shuffle(all_chars_list)

  # Select characters randomly to create the password
  password = "".join(random.choices(all_chars_list, k=length))

  return password

def main():
  """Prompts the user for desired password length and character types,
  generates a password, and displays it.
  """

  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
      break
    except ValueError:
      print("Invalid input. Please enter a number greater than or equal to 8.")

  uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
  lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
  numbers = input("Include numbers (y/n)? ").lower() == 'y'
  symbols = input("Include symbols (y/n)? ").lower() == 'y'

  try:
    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    print(f"\nGenerated password: {password}")
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
