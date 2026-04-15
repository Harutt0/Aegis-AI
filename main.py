from analyzer import calculateEntropy, isCommonPassword, getBruteForceTime, getFeedback

def runSentinel():
    # User Input
    password = input("\nEnter password to analyze (Ctrl+C to Exit): ")
    if not password:
        print("Error: Please provide a password!")
        return
    
    # Phase 1: Dictionary Attack Check
    if isCommonPassword(password):
        print("\n[!] WARNING: This password is extremely common!")
        print("Grade: 🔴 CRITICAL RISK")
        print("Estimated Crack Time: 0.0001 seconds (Known Database)")

    else:
        # Phase 2: Entropy and Brute Force Estimation
        entropy = calculateEntropy(password)
        crackTime = getBruteForceTime(password)
        
        print(f"\nPassword Strength: {entropy:.2f} bits")
        print(f"Brute Force Time: {crackTime}")
        
        # Grading Logic
        if entropy < 45:
            print("Grade: 🔴 WEAK")

        elif entropy < 70:
            print("Grade: 🟡 MEDIUM")

        else:
            print("Grade: 🟢 STRONG")
            
    # Phase 3: Improvement Recommendations
    suggestions = getFeedback(password)
    if suggestions:
        print("\nHow to improve your password:")
        for s in suggestions:
            print(s)

    else:
        print("\n✨ Perfect! Your password meets all security criteria.")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("                AGEIS-AI (V1.0)   ")
    print("="*50)

    # Infinite loop to allow multiple checks until manual exit
    try:
        while True:
            runSentinel()

    except KeyboardInterrupt:
        # Catching Ctrl+C to exit gracefully
        print("\n\nAGEIS-AI Offline. 🛡️")
