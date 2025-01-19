import os
import random
import secrets


class FileEncryptor:

    def __init__(self):
        pass

    def generate_random_key(self, length):
        return ''.join(secrets.choice('01') for _ in range(length))

    def xor_encrypt(self, data, key):
        return bytes([b ^ int(k) for b, k in zip(data, key)])

    def encrypt_file(self, input_file_path):
        with open(input_file_path, 'rb') as file:
            file_data = file.read()

        key = self.generate_random_key(len(file_data))
        encrypted_data = self.xor_encrypt(file_data, key)

        with open('key.txt', 'w') as key_file:
            key_file.write(key)

        with open('encrypted_data.txt', 'w') as encrypted_data_file:
            encrypted_data_file.write(''.join(format(byte, '08b') for byte in encrypted_data))

        os.remove(input_file_path)
        print(f"Encryption complete. Original file '{input_file_path}' destroyed.")
