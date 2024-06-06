# xOrEncryptor

# Introduction
xOrEncryptor is a simple tool for encrypting and decrypting files using the XOR encryption method. 
This method uses a symmetric key, making the encryption and decryption processes identical.
---
## Getting started 


### Prerequisites
- Python 3.6 or higher

### Installation
```console
git clone https://github.com/samuelfrnk/xOrEncryptor.git
cd xOrEncryptor
```

### Usage 
#### Encryption

Encryption From the root directory run the following command. 
```console
python3 Main.py encrypt tryout_file.png
```
Upon success the following message is shown in the commandline:
```console
Encryption complete. Original file 'tryout_file.png' destroyed.
```
> **_NOTE:_**  Please keep in mind that there is a png tryout_file included in the repository. Other/Private documents shall be encrypted with caution as it destroys the original file. 

After the encryption is complete there are two new text files "encrypted_data.txt" and "key.txt". The original file is gone. 
#### Decription

1Decryption: From the root directory run the following command.

```console
python3 Main.py decrypt key.txt encrypted_data.txt tryout_file.png
```
This will revert the XOR operation and remove both the key and encrypted data file.  

## How It Works
The XOR encryption method is a symmetric key encryption algorithm. It works by applying the XOR operation to each byte of the input file with a byte from the key. The same process is used for both encryption and decryption.
The generated key is exactly as large as the data being encrypted. Both the encrypted data and the key are stored in textfile one containing the original bytes after the  XOR operation has been applied and the key bytes.

## Considerations
This encryption method is extremely assumed the random key of 0's and 1's are generated with true randomness. 
But as proper randomness can only be ensured using a quantum computer there are natural flaws. The key is also exactly as 
large as the encrypted data which can become relevant for MP4 files. 
Finally, as with all symmetric encryption methods the problem of transmitting the key is also a drawback. 
