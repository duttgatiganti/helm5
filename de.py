import base64

# Base64 encoded string
encoded_str = "WkhCS1F1dVJoSDYtZFJiTg=="

# Decoding the base64 string
decoded_str = base64.b64decode(encoded_str).decode('utf-8')
print(decoded_str)
