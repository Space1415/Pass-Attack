import hashlib
import itertools
import string
import multiprocessing
import time

# Constants
ALGORITHMS = ['md5', 'sha256', 'sha512', 'bcrypt']
DEFAULT_DICTIONARY = "rockyou.txt"  # Replace with an actual wordlist file

# Hashing Function
def hash_password(password, algorithm='sha256'):
    if algorithm not in ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    if algorithm == 'bcrypt':
        try:
            import bcrypt
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        except ImportError:
            raise ImportError("bcrypt module not installed. Install it via pip.")
    return hashlib.new(algorithm, password.encode()).hexdigest()

# Brute Force Attack
def brute_force_attack(target_hash, algorithm='sha256', max_length=6):
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            if hash_password(attempt, algorithm) == target_hash:
                return attempt
    return None

# Dictionary Attack
def dictionary_attack(target_hash, wordlist=DEFAULT_DICTIONARY, algorithm='sha256'):
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                if hash_password(word, algorithm) == target_hash:
                    return word
    except FileNotFoundError:
        print(f"Wordlist file {wordlist} not found.")
        return None

# Rule-Based Attack
def rule_based_attack(target_hash, wordlist=DEFAULT_DICTIONARY, algorithm='sha256'):
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                transformations = generate_transformations(word)
                for transformed in transformations:
                    if hash_password(transformed, algorithm) == target_hash:
                        return transformed
    except FileNotFoundError:
        print(f"Wordlist file {wordlist} not found.")
        return None

def generate_transformations(word):
    substitutions = {'a': '@', 'o': '0', 'i': '1', 'e': '3', 's': '$'}
    variations = [word]
    for key, value in substitutions.items():
        variations += [word.replace(key, value) for key in substitutions]
    return set(variations)

# Parallel Brute Force
def parallel_brute_force(target_hash, algorithm='sha256', max_length=6):
    chars = string.ascii_letters + string.digits + string.punctuation
    pool = multiprocessing.Pool()

    for length in range(1, max_length + 1):
        args = [(target_hash, algorithm, chars, length, chunk) for chunk in split_tasks(chars, length)]
        results = pool.map(worker_brute_force, args)
        for result in results:
            if result:
                pool.close()
                return result

    pool.close()
    return None

def worker_brute_force(args):
    target_hash, algorithm, chars, length, chunk = args
    for attempt in itertools.product(chunk, repeat=length):
        attempt = ''.join(attempt)
        if hash_password(attempt, algorithm) == target_hash:
            return attempt
    return None

def split_tasks(chars, length):
    step = len(chars) // multiprocessing.cpu_count()
    return [chars[i:i + step] for i in range(0, len(chars), step)]

# Main Function
def main():
    print("Password Attack Simulator")
    print("1. Brute Force Attack")
    print("2. Dictionary Attack")
    print("3. Rule-Based Attack")
    print("4. Parallel Brute Force Attack")
    choice = int(input("Select an option: "))

    target_password = input("Enter target password to hash: ")
    algorithm = input(f"Select algorithm ({', '.join(ALGORITHMS)}): ")
    target_hash = hash_password(target_password, algorithm)

    start_time = time.time()

    if choice == 1:
        cracked = brute_force_attack(target_hash, algorithm)
    elif choice == 2:
        cracked = dictionary_attack(target_hash, DEFAULT_DICTIONARY, algorithm)
    elif choice == 3:
        cracked = rule_based_attack(target_hash, DEFAULT_DICTIONARY, algorithm)
    elif choice == 4:
        cracked = parallel_brute_force(target_hash, algorithm)
    else:
        print("Invalid option.")
        return

    end_time = time.time()

    if cracked:
        print(f"Password cracked: {cracked}")
    else:
        print("Failed to crack the password.")

    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
