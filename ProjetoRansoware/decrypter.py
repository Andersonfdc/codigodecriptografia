import os
import pyaes

## ABRIR ARQUIVO CRIPTOGRAFADO

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## CHAVE DA CRIPTOGRAFIA

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## REMOVER 0 ARQUIVO CRIPTOGRAFADO

os.remove(file_name)

## CRIAR UM NOVO ARQUIVO

new_file = "teste.txt"
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
