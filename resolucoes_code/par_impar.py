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
# O objetivo deste código é solicitar ao usuário que insira um número inteiro,
# verificar se esse número é par ou ímpar e exibir o resultado no console.
# Este exemplo é útil para entender conceitos básicos de utilização de condicionais em Python.

# 🤔 Uma string é uma sequência de caracteres, como palavras ou frases. 
# No Python, strings são delimitadas por aspas simples ('') ou duplas ("").

# 🔡 Variável: Uma variável é um espaço na memória que armazena um valor.
# No Python, as variáveis são criadas automaticamente quando você atribui um valor a elas.
# Por exemplo, `numero` é uma variável que armazena o valor inserido pelo usuário.

# ⌨️ Solicitação da entrada de dados do usuário
# A função input() é usada para capturar a entrada do usuário.
# O texto dentro dos parênteses é exibido como um prompt para o usuário.
# int(): Converte uma string ou número em um número inteiro.
numero = int(input("Digite um número inteiro: "))

# 🔢 Verifica se o número é par ou ímpar
# O operador de módulo (%) retorna o resto da divisão de um número pelo outro.
# Se o resto da divisão de um número por 2 for 0, o número é par. Caso contrário, é ímpar.
# if: Verifica uma condição. Se a condição for verdadeira, o bloco de código associado ao if será executado.
if numero % 2 == 0:
    resultado = "O número é par."
# else: Executa um bloco de código se a condição do if for falsa.
else:
    resultado = "O número é ímpar."

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
# 4. Navegue até o diretório onde o arquivo `par_impar.py` está localizado usando o comando `cd`.
#    Exemplo: cd C:/Users/usuário/OneDrive/Desktop
# 5. Execute o código Python usando o comando `python` seguido do nome do arquivo.
#    Exemplo: python par_impar.py
# 6. Interaja com o programa inserindo um número inteiro quando solicitado.
# 7. Veja o resultado exibido no console.