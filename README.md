🛡️ AEGIS-AI

AEGIS-AI is a high-performance, mathematically-driven security auditing tool developed in Python. It evaluates password integrity by merging Shannon's Information Theory with real-world attack simulations to provide a comprehensive security score.

🎯 Project Overview

The objective of this project is to move beyond simple character counting. AEGIS-AI demonstrates how Cryptographic Entropy and Dictionary Heuristics can be applied to cybersecurity to identify weak links before they are exploited. It transforms raw strings into actionable security intelligence.

✨ Key Features

Entropy-Driven Scoring: Uses Shannon's Entropy formula to measure the mathematical unpredictability of a password.

Leak Intelligence: Cross-references inputs against high-frequency leaked password databases (passwords.txt) for instant vulnerability detection.

Brute-Force ETA: Calculates the time complexity required to crack the password based on a benchmark of 10 billion guesses per second.

Pattern Recognition: Optimized Regex engine to detect character variety (Uppercase, Lowercase, Digits, and Symbols) in real-time.

Clean Architecture: Developed with an Early Return pattern to ensure high performance and code readability.

🚀 Getting Started

1. Installation

Clone the repository to your local machine:
git clone https://github.com/Harutt0/Aegis-AI.git
cd Aegis-AI

2. Install Dependencies

Install the required data processing libraries:
pip install -r requirements.txt

3. Run Analysis

Launch the security auditor:
python main.py

🛠️ Technical Specifications

Note: This project prioritizes cryptographic depth. It calculates the "Bit-Strength" of a password to determine its resistance against modern computing power.

Core Engine: High-performance entropy calculation based on $log_2(L^R)$ to determine mathematical strength.

Pool Analysis: Dynamic evaluation of character set depth ($26, 52, 62,$ or $94$ characters).

Scalability: Optimized to process massive dictionary files using efficient I/O operations without memory overhead.

🙏 Acknowledgements

Cryptographic Research: Inspired by the NIST guidelines for password complexity and entropy estimation models.
Python Developers: Thanks to the creators of pandas and the standard library modules for a robust ecosystem.
Security Researchers: Dedicated to the white-hat hackers who work to build a safer web for everyone.

🛡️ Final Note

Thank you for checking out AEGIS-AI! This tool was engineered to bridge the gap between mathematical entropy and practical defense logic. If you find this tool useful for your security audits or research, feel free to leave a ⭐.

Developed with passion for a safer web by Harutt0 🚀
