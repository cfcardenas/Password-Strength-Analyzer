import re


def check_password_strength(password):
    feedback = []
    suggestions = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
        suggestions.append("- Consider making the password at least 12 characters long.")

    # Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        feedback.append("Password must contain at least one uppercase letter.")
        suggestions.append("- Use at least one uppercase letter.")

    # Check for lowercase letters
    if not re.search(r"[a-z]", password):
        feedback.append("Password must contain at least one lowercase letter.")
        suggestions.append("- Use at least one lowercase letter.")

    # Check for numbers
    if not re.search(r"[0-9]", password):
        feedback.append("Password must contain at least one number.")
        suggestions.append("- Add at least one number (e.g., 1, 2, 3).")

    # Check for special characters
    if not re.search(r"[^a-zA-Z0-9]", password):
        feedback.append("Password must contain at least one special character.")
        suggestions.append("- Include at least one special character (e.g., !, @, #).")

    # Check for repeating characters consecutively
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating characters consecutively more than twice.")
        suggestions.append("- Avoid consecutive repeating characters.")

    # Check for unique characters
    if len(set(password)) < 6:
        feedback.append("Password should contain at least 6 unique characters.")
        suggestions.append("- Try to use more unique characters to increase complexity.")

    # Determine final strength message and provide suggestions
    if feedback:
        return f"Weak: {', '.join(feedback)}\nSuggestions: \n" + "\n".join(suggestions)

    return "Strong: Password meets all complexity requirements."


# Loop to allow the user to reattempt until a strong password is entered
while True: 
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

    if "Strong" in result:
        break  # Exit the loop if the password is strong
    else:
        print("Please try again with a stronger password.\n")

# Note: This script is a simple password strength checker and should not be used as a replacement for secure password storage or management practices.
# It is recommended to use a password manager for secure password storage.

        
