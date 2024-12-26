Password Attack Simulator

Overview

The Password Attack Simulator is an educational tool designed to demonstrate how common password attacks work. It aims to help users understand the importance of strong passwords and the techniques used in ethical hacking to test password security.

This simulator supports multiple attack methods and hashing algorithms to provide a comprehensive learning experience. It is intended for educational purposes only and should not be used for malicious activities.

Features

Brute Force Attack: Attempts all possible combinations of characters up to a specified length.

Dictionary Attack: Uses a wordlist to try known passwords.

Rule-Based Attack: Applies transformations like character substitution (e.g., a -> @) to dictionary words.

Parallel Brute Force: Leverages multiprocessing to speed up brute force attacks.

Hashing Algorithms: Supports MD5, SHA-256, SHA-512, and bcrypt.

Requirements

Python 3.7+

Libraries:

hashlib (standard library)

bcrypt (optional, install via pip install bcrypt)

multiprocessing (standard library)

Installation

Clone the repository:

git clone https://github.com/your-username/password-attack-simulator.git
cd password-attack-simulator

(Optional) Install the bcrypt library for bcrypt support:

pip install bcrypt

Usage

Run the simulator using:

python password_attack_simulator.py

Example Workflow

Select an attack method from the menu:

Brute Force

Dictionary Attack

Rule-Based Attack

Parallel Brute Force

Provide the target password to hash and the hashing algorithm.

The program will attempt to crack the password and display the result.

Wordlist

For dictionary and rule-based attacks, you can use your own wordlist file. Replace the default rockyou.txt file with your preferred wordlist.

File Structure

password_attack_simulator.py: Main program.

rockyou.txt: Example wordlist (not included; download separately if needed).

Ethical Disclaimer

This tool is strictly for educational purposes. Misuse of this tool for unauthorized password cracking or malicious purposes is illegal and unethical. Always ensure you have permission before conducting any security testing.

Future Enhancements

Add GUI for better usability.

Support for additional hashing algorithms.

Integration with real-world password strength analyzers.

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

Inspired by ethical hacking and cybersecurity practices.

Utilizes the Python standard library and open-source libraries.

