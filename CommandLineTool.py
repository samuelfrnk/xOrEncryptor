import argparse

from FileDecryptor import FileDecryptor
from FileEncryptor import FileEncryptor


class CommandLineTool:
    def __init__(self):
        self.encryptor = FileEncryptor()
        self.decryptor = FileDecryptor()

    def run(self):
        parser = argparse.ArgumentParser(description="Encrypt and Decrypt files using XOR encryption.")
        subparsers = parser.add_subparsers(dest="command")

        encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file.')
        encrypt_parser.add_argument('input_file', type=str, help='Path to the input file to be encrypted.')

        decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt files.')
        decrypt_parser.add_argument('key_file', type=str, help='Path to the key file.')
        decrypt_parser.add_argument('encrypted_data_file', type=str, help='Path to the encrypted data file.')
        decrypt_parser.add_argument('output_file', type=str, help='Path to the output decrypted file.')

        args = parser.parse_args()

        if args.command == 'encrypt':
            self.encryptor.encrypt_file(args.input_file)
        elif args.command == 'decrypt':
            self.decryptor.decrypt_file(args.key_file, args.encrypted_data_file, args.output_file)
        else:
            parser.print_help()
