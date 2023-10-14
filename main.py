# Importação da(s) biblioteca(s)

from tkinter import *

# Cores

cor_fundo = '#202020'
cor_botao = 'gray'
cor_letra = 'black'

# Configurações da janela

janela = Tk() # Instância do objecto janela

janela.title('Calculadora') # Configuração do título da janela
janela.geometry('486x486') # Configuração da dimensão da janela (Largura e Altura)
janela.configure(background=cor_fundo) # Configuração da cor de fundo da janela
janela.resizable(width=False, height=False) # Redimensionamento da janela (Largura e Altura)

janela.iconphoto(False, PhotoImage(file=r'images/icon-calculadora-58x58.png')) # Configuração do ícone da janela

# Criação das variáveis globais

expressao = ''
resultado_zero = False

# Criação das funções

def limparTela():

    '''
    Esta função vai limpar a tela removendo todos os valores do label resultado, ou seja
    colocando uma string vazia na propriedade 'text' do label resultado.
    '''

    label_resultado["text"] = ''
    expressao == ''


def removerCaracter():

    '''
    Esta função vai fazer o label resultado receber o valor do mesmo label resultado, só que sem o último caracter digitado.
    
    O '[:-1]' indica que a string será fatiada indo do início até ao fim, só que em Python o último elemento de um intervalo nunca é considerado, então o último elemento irá ser descartado. 
    '''
    
    global expressao
    expressao = expressao[:-1]
    label_resultado["text"] = expressao


def mostrarResultado(valor):

    '''
    Esta função irá fazer com que aprensente na tela (label resultado) o valor dos botões correspondentes clicados e o resultado dos cálculos obtidos.
    '''

    global expressao
    global resultado_zero
    
    if label_resultado["text"] == 'ERROR' or resultado_zero == True:
        limparTela()
        resultado_zero = False
            
    expressao = label_resultado["text"]
    expressao += valor
    label_resultado["text"] = expressao
    
def calcularPorcentagem():

    '''
    Esta função é apenas para calcular a porcentagem de um número.
    '''
    
    global expressao
    
    if ',' in expressao:
        expressao = expressao.replace(',', '.')
        expressao = float(expressao)
    else:
        expressao = int(expressao)
        
    expressao = expressao / 100
    expressao = str(expressao)
    
    if '.' in expressao:
        expressao = expressao.replace('.', ',')
            
    if ',0' in expressao:
        expressao = expressao.replace(',0', '')
    
    label_resultado["text"] = expressao

def Calcular():

    '''
    Esta função irá calcular o resultado da expressão matemática inserida no label resultado. Usando a função 'eval()' que verifica a expressão e faz o cálculo.
    '''

    global expressao
    global resultado_zero
    
    try:

        if 'x' in expressao:
            expressao = expressao.replace('x', '*')
        
        if ',' in expressao:
            expressao = expressao.replace(',', '.')
            
        elif '²' in expressao:
            expressao = expressao.replace('²', '**2')
            
        elif '√' in expressao[0]:
            expressao = expressao.replace('√', '')
            expressao = expressao + '**(1/2)'
            
        resultado = eval(expressao)
        
        if resultado == 0:
            resultado_zero = True
        
        resultado = str(resultado)
        
    except:
        label_resultado["text"] = "ERROR"
        
    else:
        
        if '.' in resultado:
            resultado = resultado.replace('.', ',')
            
        if ',0' in resultado:
            resultado = resultado.replace(',0', '')
            
        expressao = resultado
        label_resultado["text"] = resultado
    
    

# Configuração do Label do resultado

    # Será neste label que irá ser aprensentado o resultado de tudo que for calculado

label_resultado = Label(janela, width=31, height=5, background='#262525', font='Ivy 15 bold',foreground='white', anchor=SE)
label_resultado.place(x=23, y=30)

# Configuração dos botões

    # linha 1

btn_abrir_parenteses = Button(janela, text='(', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=lambda:mostrarResultado('('))
btn_abrir_parenteses.place(x=23, y=200)

btn_fechar_parenteses = Button(janela, text=')', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=lambda:mostrarResultado(')'))
btn_fechar_parenteses.place(x=125, y=200)

btn_limpar = Button(janela, text='C', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=limparTela)
btn_limpar.place(x=227, y=200)

btn_remover = Button(janela, text='<=', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=removerCaracter)
btn_remover.place(x=329, y=200)

    # linha 2

btn_porcentagem = Button(janela, text='%', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=calcularPorcentagem)
btn_porcentagem.place(x=23, y=243)
 
btn_potencia = Button(janela, text='x²', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=lambda:mostrarResultado('²'))
btn_potencia.place(x=125, y=243)

btn_raiz_quadrada = Button(janela, text='√', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=lambda: mostrarResultado('√'))
btn_raiz_quadrada.place(x=227, y=243)

btn_dividir = Button(janela, text='/', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=lambda: mostrarResultado('/'))
btn_dividir.place(x=329, y=243)

    # linha 3

btn_n_7 = Button(janela, text='7', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('7'))
btn_n_7.place(x=23, y=286)

btn_n_8 = Button(janela, text='8', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('8'))
btn_n_8.place(x=125, y=286)

btn_n_9 = Button(janela, text='9', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('9'))
btn_n_9.place(x=227, y=286)

btn_multiplicar = Button(janela, text='x', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda: mostrarResultado('x'))
btn_multiplicar.place(x=329, y=286)

    # linha 4
    
btn_n_4 = Button(janela, text='4', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('4'))
btn_n_4.place(x=23, y=329)

btn_n_5 = Button(janela, text='5', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('5'))
btn_n_5.place(x=125, y=329)

btn_n_6 = Button(janela, text='6', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('6'))
btn_n_6.place(x=227, y=329)

btn_subtrair = Button(janela, text='-', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=lambda: mostrarResultado('-'))
btn_subtrair.place(x=329, y=329)

    # linha 5
    
btn_n_1 = Button(janela, text='1', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('1'))
btn_n_1.place(x=23, y=372)

btn_n_2 = Button(janela, text='2', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('2'))
btn_n_2.place(x=125, y=372)

btn_n_3 = Button(janela, text='3', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('3'))
btn_n_3.place(x=227, y=372)

btn_n_somar = Button(janela, text='+', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9', command=lambda:mostrarResultado('+'))
btn_n_somar.place(x=329, y=372)

    # linha 6
    
btn_n_0 = Button(janela, text='0', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=23, height=2, font='Ivy 9 bold', command=lambda:mostrarResultado('0'))
btn_n_0.place(x=23, y=415)

btn_virgula = Button(janela, text=',', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=12, height=2, font='Ivy 9 bold', command=lambda:mostrarResultado(','))
btn_virgula.place(x=228, y=415)

btn_igual = Button(janela, text='=', relief='raised', overrelief='ridge', foreground=cor_letra, background=cor_botao, width=13, height=2, font='Ivy 9 bold', command=Calcular)
btn_igual.place(x=329, y=415)

janela.mainloop() # Método para manter a janela sempre aberta
