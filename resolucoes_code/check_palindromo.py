# 🐍 Este código está escrito em Python, uma linguagem de programação de alto nível,
# conhecida por sua simplicidade e legibilidade. Python é amplamente utilizado
# para desenvolvimento web, automação, análise de dados, inteligência artificial,
# entre outras áreas.

# 💻 Este código foi escrito numa IDE chamada Visual Studio Code.
# IDE (Integrated Development Environment) é um ambiente de desenvolvimento integrado
# que fornece ferramentas abrangentes para escrever, testar e depurar código.
# Visual Studio Code é uma IDE popular que suporta várias linguagens de programação
# e oferece recursos como destaque de sintaxe, autocompletar, e integração com sistemas de controle de versão.

# 👤 Este código foi escrito e codificado por João Teixeira
# github.com/joaocvteixeira
# linkedin.com/in/joaocvteixeira

# 🎯 Objetivo do código:
# O objetivo deste código é solicitar ao usuário que insira uma palavra,
# verificar se essa palavra é um palíndromo e exibir o resultado no console.
# Este exemplo é útil para entender conceitos básicos de manipulação de strings em Python.

# 📚 O que é um palíndromo?
# Um palíndromo é uma palavra, frase, número ou qualquer outra sequência de caracteres
# que lê da mesma forma de trás para frente (ignorando espaços, pontuação e diferenças de maiúsculas/minúsculas).
# Exemplos de palíndromos incluem "radar", "level", "rotor".

# 🤔 Uma string é uma sequência de caracteres, como palavras ou frases. 
# No Python, strings são delimitadas por aspas simples ('') ou duplas ("").

# 🔡 Variável: Uma variável é um espaço na memória que armazena um valor.
# Em Python, você pode criar uma variável simplesmente atribuindo um valor a um nome usando o operador de atribuição (=).
# Exemplo: nome_da_variavel = valor
# No código abaixo, a variável 'palavra' armazena a entrada do usuário.

# ⌨️ Solicitação da entrada de dados do usuário
# A função input() é usada para capturar a entrada do usuário.
# O texto dentro dos parênteses é exibido como um prompt para o usuário.
palavra = input("Digite uma palavra: ")

# 🔄 Inverte a string
# A sintaxe [::-1] é usada para inverter a string.
palavra_invertida = palavra[::-1]

# 🔍 Verifica se a palavra é um palíndromo
# Compara a string original com sua versão invertida.
if palavra == palavra_invertida:
    resultado = "A palavra é um palíndromo."
else:
    resultado = "A palavra não é um palíndromo."

# 🖨️ Exibe o resultado da verificação
# A função print() é usada para exibir a saída no console.
# Console é a interface onde os resultados do código são exibidos.
print(resultado)

# ▶️ Como rodar este código:
# 1. Requer instalar Python:
#    - Acesse o site oficial do Python: https://www.python.org/
#    - Baixe e instale a versão mais recente do Python.
#    - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.
# 2. Abra o Visual Studio Code.
# 3. Abra o terminal integrado pressionando `Ctrl + `` (Ctrl + acento grave) ou indo em `Terminal` > `Novo Terminal`
#    geralmente encontrado na parte superior da tela. Certifique-se que o terminal está definido para Python
#    (e não PowerShell por exemplo...)
# 4. Navegue até o diretório onde o arquivo `check_palindromo.py` está localizado usando o comando `cd`.
#    Exemplo: cd C:/Users/usuário/OneDrive/Desktop
# 5. Execute o código Python usando o comando `python` seguido do nome do arquivo.
#    Exemplo: python check_palindromo.py
# 6. Interaja com o programa inserindo uma palavra quando solicitado.
# 7. Veja o resultado exibido no console.