# CÓDIGO DE CRIPTOGRAFICA COM PYTHON

## Explicação do Código:

- Primeiro, importamos as bibliotecas necessárias, incluindo os para operações de sistema de arquivos e ``` pyaes ``` para a criptografia AES.

- Em seguida, especificamos o nome do arquivo criptografado que desejamos descriptografar (no exemplo, ``` teste.txt.ransowaretroll ```) e abrimos o arquivo em modo de leitura binária ```('rb')```.

- Definimos uma chave secreta (key) que é usada para descriptografar o arquivo. Certifique-se de que a chave seja a mesma usada para criptografar o arquivo originalmente.

- Utilizamos a biblioteca pyaes para descriptografar os dados do arquivo com a chave especificada. O resultado é armazenado na variável ```decrypt_data```.

- Removemos o arquivo criptografado original usando a função ```os.remove()``` para evitar que o arquivo não criptografado e o arquivo criptografado coexistam.

- Por fim, criamos um novo arquivo chamado ```'teste.txt'``` e escrevemos os dados descriptografados nele em modo binário. O arquivo descriptografado agora está disponível em sua forma original.
