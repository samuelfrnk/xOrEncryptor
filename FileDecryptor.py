import os
import random
class FileDecryptor():
    def __init__(self):
        pass
    def binary_string_to_bytes(self, binary_string):
        byte_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        return bytes([int(b, 2) for b in byte_list])

    def xor_decrypt(self, data, key):
        return bytes([b ^ int(k) for b, k in zip(data, key)])

    def decrypt_file(self, key_file_path, encrypted_data_file_path, output_file_path):
        with open(key_file_path, 'r') as key_file:
            key = key_file.read()
        
        with open(encrypted_data_file_path, 'r') as encrypted_data_file:
            encrypted_data_binary = encrypted_data_file.read()

        encrypted_data = self.binary_string_to_bytes(encrypted_data_binary)
        decrypted_data = self.xor_decrypt(encrypted_data, key)

        with open(output_file_path, 'wb') as output_file:
            output_file.write(decrypted_data)
        os.remove(encrypted_data_file_path)
        os.remove(key_file_path)
        print(f"Decryption complete. Decrypted file saved as '{output_file_path}'.")
