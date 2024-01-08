import base64

# Encrypt password

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)


encode_string = input("Enter your password: ")
encrypt_pass(encode_string)

# Dencrypt password

def decode_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password: {decode_data}")


encode_string = input("Copy the base64 string and paste it here: ")
decode_pass(encode_string)
