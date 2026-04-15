import re
import math

def calculateEntropy(password):
    # Formula: Strength = Password Length * log2(Character Pool Size)
    charPool = 0

    # Check for lowercase letters (a-z = 26)
    if re.search(r'[a-z]', password):
        charPool += 26

    # Check for uppercase letters (A-Z = 26)
    if re.search(r'[A-Z]', password):
        charPool += 26

    # Check for numbers (0-9 = 10)
    if re.search(r'[0-9]', password):
        charPool += 10

    # Check for special characters (approx. 32)
    if re.search(r'[^a-zA-Z0-9]', password):
        charPool += 32
    
    if charPool == 0 or len(password) == 0: 
        return 0
        
    # Bit entropy calculation
    return len(password) * math.log2(charPool)

def isCommonPassword(password, file_path="passwords.txt"):
    # Checks if the password exists in a list of most common/leaked passwords
    try:
        with open(file_path, "r") as f:
            commonPasswords = f.read().splitlines()
        return password in commonPasswords
    
    except FileNotFoundError:
        # If file is missing, return False but log a warning in a real app
        return False

def getBruteForceTime(password):
    # Estimates the time required to crack the password using a Brute Force attack
    charPool = 0
    if re.search(r'[a-z]', password):
        charPool += 26

    if re.search(r'[A-Z]', password):
        charPool += 26

    if re.search(r'[0-9]', password):
        charPool += 10

    if re.search(r'[^a-zA-Z0-9]', password):
        charPool += 32
    
    if charPool == 0 or len(password) == 0:
        return "0 seconds"
    
    # Total possible combinations: Pool Size ^ Length
    combinations = math.pow(charPool, len(password))

    # 10,000,000,000 guesses per second (High-end GPU clusters)
    seconds = combinations / 10_000_000_000
    
    # Human-readable time formatting
    if seconds < 1:
        return "Instant (Less than 1 sec)"
    
    if seconds < 60:
        return f"{int(seconds)} seconds"
    
    if seconds < 3600:
        return f"{int(seconds/60)} minutes"
    
    if seconds < 86400:
        return f"{int(seconds/3600)} hours"
    
    if seconds < 31536000:
        return f"{int(seconds/86400)} days"
    
    if seconds < 31536000000:
        return f"{int(seconds/31536000)} years"
    return "Centuries (Virtually Unbreakable!)"

def getFeedback(password):
    # Provides specific security advice based on the weaknesses of the password
    tips = []
    if len(password) < 12:
        tips.append("- Increase length to at least 12 characters.")

    if not re.search(r'[A-Z]', password):
        tips.append("- Add at least one uppercase letter (A-Z).")

    if not re.search(r'[0-9]', password):
        tips.append("- Include at least one number (0-9).")

    if not re.search(r'[^a-zA-Z0-9]', password):
        tips.append("- Use special characters (e.g., !, @, #, $).")
    return tips
