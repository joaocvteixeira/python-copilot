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
# O objetivo deste código é solicitar ao usuário que insira seu nome, idade e cidade,
# concatenar essas informações em uma string formatada e exibi-la no console.
# Isso demonstra como capturar entradas do usuário, armazená-las em variáveis,
# e combiná-las em uma mensagem legível. Este exemplo é útil para entender
# conceitos básicos de entrada e saída em Python.

# 🤔 Uma string é uma sequência de caracteres, como palavras ou frases. 
# No Python, strings são delimitadas por aspas simples ('') ou duplas ("").

# 🔡 Variável: Uma variável é um espaço na memória que armazena um valor. 
# No código abaixo, 'nome', 'idade' e 'cidade' são variáveis que armazenam 
# as entradas fornecidas pelo usuário. Variáveis são essenciais em programação 
# pois permitem que os dados sejam manipulados e utilizados ao longo do código.

# ⌨️ Solicitação das entradas de dados do usuário
# A função input() é usada para capturar a entrada do usuário. 
# O texto dentro dos parênteses é exibido como um prompt para o usuário.
# Prompt nesse código é uma mensagem ou instrução exibida para o usuário, indicando que ele deve 
# fornecer alguma entrada.
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")

# 🔡 Variável: Uma variável é um espaço na memória que armazena um valor. 
# No código acima, 'nome', 'idade' e 'cidade' são variáveis que armazenam 
# as entradas fornecidas pelo usuário.

# 🔗 Concatenar nesse código significa unir duas ou mais strings em uma única string.
# Aqui, estamos concatenando as strings "Nome: ", "Idade: ", e "Cidade: " 
# com as entradas fornecidas pelo usuário.
# O operador + é usado para concatenar strings.
resultado = nome + " de " + idade + " anos, da cidade de " + cidade + " testou esse código!"

# 🖨️ Exibe a string concatenada
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
# 4. Navegue até o diretório onde o arquivo `concat_dados.py` está localizado usando o comando `cd`.
#    Exemplo: cd C:/Users/usuário/OneDrive/Desktop
# 5. Execute o código Python usando o comando `python` seguido do nome do arquivo.
#    Exemplo: python concat_dados.py
# 6. Interaja com o programa inserindo seu nome, idade e cidade quando solicitado.
# 7. Veja o resultado exibido no console.
