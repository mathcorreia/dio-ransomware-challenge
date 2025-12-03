import os
import pyaes

def decrypt_file(encrypted_file_name, key):
    try:
        # 1. Abrir o arquivo criptografado
        with open(encrypted_file_name, "rb") as file:
            file_data = file.read()

        # 2. Configurar a descriptografia com a MESMA chave
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # 3. Remover o arquivo criptografado
        os.remove(encrypted_file_name)

        # 4. Restaurar o arquivo original
        original_file_name = "teste.txt"
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"[SUCESSO] Arquivo restaurado para '{original_file_name}'.")

    except FileNotFoundError:
        print(f"[ERRO] Arquivo criptografado '{encrypted_file_name}' não encontrado.")
    except Exception as e:
        print(f"[ERRO] Falha na descriptografia: {e}")

# A chave deve ser EXATAMENTE a mesma usada no encrypter
key = b"testeransomwares"
encrypted_file = "teste.txt.ransomwaretroll"

decrypt_file(encrypted_file, key)
