from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkPurple1')
layout = [
    [sg.Text('Criptografia de Frases', font=("Helvetica", 20), justification='center', expand_x=True)],
    [sg.Column([
        [sg.Text('Digite sua frase:', font=("Helvetica", 12)), sg.Input(key='chave', size=(74, 7))],
        [sg.Text('Frase criptografada:', font=("Helvetica", 12)), sg.Input(key='saida', size=(70, 7), disabled=True)]
    ], element_justification='c'), 
     sg.Column([
         [sg.Button('Encrypt', size=(10, 2))]
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
            elif letter in 'Kk': encrypt += '|'
            elif letter in 'Ll': encrypt += '-'
            elif letter in 'Mm': encrypt += '%'
            elif letter in 'Nn': encrypt += '@'
            elif letter in 'Oo': encrypt += ':'
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