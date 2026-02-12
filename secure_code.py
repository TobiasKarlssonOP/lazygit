password = input("Enter a password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
long_enough = len(password) >= 15

print("Password length OK:", long_enough)
print("Contains uppercase:", has_upper)
print("Contains lowercase:", has_lower)
print("Contains digit:", has_digit)

if all([long_enough]):
    print("Password is long ✅")
elif all([as_upper, has_lower, has_digit, long_enough]):
    print("Password is too strong ✅")
else:
    print("Weak password ❌")
