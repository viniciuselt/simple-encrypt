from PySimpleGUI import PySimpleGUI as sg

# Dicionário de criptografia
dicionario_criptografia = {
    'A': '4',
    'B': '8',
    'C': 'ç',
    'D': '0',
    'E': '3',
    'F': '*',
    'G': '¨',
    'H': '&',
    'I': '5',
    'J': '%',
    'K': '()',
    'L': '1',
    'M': '%',
    'N': '@',
    'O': '*',
    'P': '#',
    'Q': '+',
    'R': '!',
    'S': '>',
    'T': '^',
    'U': '<',
    'V': ';'
}

# Cria a caixa de dicionário
dicionario_layout = [
    [sg.Text('Dicionário da criptografia', font=("Helvetica", 14))],
    [sg.Column([
        [sg.Text(key, size=(3, 1)), sg.Text(value, size=(3, 1))] 
        for key, value in dicionario_criptografia.items()
    ])]
]
dicionario_janela = sg.Window('Dicionário de criptografia', dicionario_layout, finalize=True)
dicionario_janela.hide()

# Layout
sg.theme('DarkPurple1')
layout = [
    [sg.Text('Criptografia de Frases', font=("Helvetica", 20), justification='center', expand_x=True)],
    [sg.Column([
        [sg.Text('Digite sua frase:', font=("Helvetica", 12)), sg.Input(key='chave', size=(74, 7))],
        [sg.Text('Frase criptografada:', font=("Helvetica", 12)), sg.Input(key='saida', size=(70, 7), disabled=True)]
    ], element_justification='c'), 
     sg.Column([
         [sg.Button('Encrypt', size=(10, 2))],
         [sg.Button('Dicionário', size=(10, 2))]
     ], element_justification='c')]
]

# Janela
janela = sg.Window('Criptografia Simples', layout)

# Ler os eventos
while True:
    events, valores = janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Encrypt':
        chave = valores['chave']
        encrypt = ''
        for letter in chave:
            if letter in dicionario_criptografia:
                encrypt += dicionario_criptografia[letter]
            if letter in 'Aa': encrypt += '4'  
            elif letter in 'Bb': encrypt += '8'  
            elif letter in 'Cc': encrypt += 'ç' 
            elif letter in 'Dd': encrypt += '0'   
            elif letter in 'Ee': encrypt += '3'  
            elif letter in 'Ff': encrypt += '*'
            elif letter in 'Gg': encrypt += '¨'
            elif letter in 'Hh': encrypt += '&'
            elif letter in 'Ii': encrypt += '5'
            elif letter in 'Jj': encrypt += '%'
            elif letter in 'Kk': encrypt += '()'
            elif letter in 'Ll': encrypt += '1'
            elif letter in 'Mm': encrypt += '%'
            elif letter in 'Nn': encrypt += '@'
            elif letter in 'Oo': encrypt += '*'
            elif letter in 'Pp': encrypt += '#'
            elif letter in 'Qq': encrypt += '+'
            elif letter in 'Rr': encrypt += '!'
            elif letter in 'Ss': encrypt += '>'
            elif letter in 'Tt': encrypt += '^'
            elif letter in 'Uu': encrypt += '<'
            elif letter in 'Vv': encrypt += ';'
            else:
                encrypt += letter
        janela['saida'].update(encrypt)
        print(f'A criptografia gerada para sua frase foi: {encrypt}')
    if events == 'Dicionário':
        dicionario_janela.un_hide()