import random
import string

tam = int(input("Escolha um tamanho:" ))

def generate_password (tam):
  carac = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(carac) for i in range(tam))

  return password

print(generate_password(tam))