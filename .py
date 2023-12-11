import itertools

def generate_passwords(wordlist, max_length):
    passwords = []
    for length in range(1, max_length + 1):
        for combination in itertools.product(wordlist, repeat=length):
            password = ''.join(combination)
            passwords.append(password)
    return passwords

if __name__ == '__main__':
    wordlist = ['password', '123', 'qwerty', 'admin']
    max_length = 4
    passwords = generate_passwords(wordlist, max_length)
    print(passwords)
