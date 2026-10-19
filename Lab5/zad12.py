import hashlib

def sign(message, private_key):
    text = message + private_key
    return hashlib.sha256(text.encode()).hexdigest()

def verify(message, private_key, signature):
    return sign(message, private_key) == signature

message = "Transfer 10 coins"
private_key = "my_secret_key"

signature = sign(message, private_key)

print("Подпись:", signature)
print("Проверка верной подписи:",
      verify(message, private_key, signature))

changed_message = "Transfer 100 coins"

print("Проверка при подмене сообщения:",
      verify(changed_message, private_key, signature))