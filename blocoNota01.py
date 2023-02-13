#
# autores:
# Michel

# data: 08/02/2023


import tkinter
from tkinter.filedialog import askopenfilename # para poder abrir um arquivo
from tkinter.filedialog import asksaveasfilename # para poder salvar um arquivo

def novo():
  areaTexto.delete(1.0, "end") #deletar toda area de texto 

def salvar():
  #1 areaTexto.get(1.0, "end") # 1 pegamos tudo do inicio 1.0 ao fim
  conteudo = areaTexto.get(1.0, "end") # 2 criamos uma variável para pode guardar esse conteúdo
  arquivo1 = open("BlocoNota.txt", 'w') # para podemos abrir o arquivo para poder gravar nele
  arquivo1.write(conteudo) # gravo no arquivo
  arquivo1.close() # fecho o arquivo

def salvarComo():
  nomeArquivo = asksaveasfilename() 
  conteudo = areaTexto.get(1.0, "end") # 2 criamos uma variável para pode guardar esse conteúdo
  arquivo1 = open(nomeArquivo, 'w') # para podemos abrir o arquivo para poder gravar nele
  arquivo1.write(conteudo.rstrip()) # gravo no arquivo
  #arquivo1.close() # fecho o arquivo
  

def abrir():
  nomeArquivo = askopenfilename()
#  print("abrir")
  arquivo1 = open(nomeArquivo, 'r')
  conteudo = arquivo1.read()
  areaTexto.insert(1.0, conteudo)


#janela1
janela1 = tkinter.Tk()  # crio o objeto janela1
janela1.title("Meu Bloco de Notas")  # titulo da janela1
# o geometry(valor1xvalor2) define um tamanho inicial da janela1
janela1.geometry("300x200") # com o geometry posso redimensionar a janela1 usando o mouse
janela1.minsize(width=300, height=200) # defino o tamanho mínimo da janela1

# contêiner de texto 
areaTexto = tkinter.Text(janela1, font="Arial 20 bold", width=300, height=200)
areaTexto.pack()

#menu principal
menuPrincipal = tkinter.Menu(janela1)

#sub menu
arquivoMenu = tkinter.Menu(menuPrincipal, tearoff=0) # tearoff por padrão vem 1, vamos def igual a 0, para não aparecer uma linha no menu principal 
arquivoMenu.add_command(label="Novo", command=novo) # quando click ele chama uma função
arquivoMenu.add_command(label="Salvar", command=salvar)
arquivoMenu.add_command(label="Salvar como...", command=salvarComo)
arquivoMenu.add_command(label="abrir", command=abrir)
arquivoMenu.add_command(label="Sair", command=janela1.quit)

menuPrincipal.add_cascade(label="Arquivo", menu=arquivoMenu) # quando click no botão vai abrir um leque de opções
janela1.config(menu=menuPrincipal)


janela1.mainloop()  #loop do objeto janela1
