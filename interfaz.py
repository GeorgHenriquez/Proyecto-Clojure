import tkinter as tk
from lexico_clojure import analizar
from sintactico_clojure import parser


class Ventana:
    root = None
    def __init__(self, root):
        root = root
        root.title("Analizador de Sintaxis")
        
        self.titulo = tk.Label(root, text="CLOJURE", font="45")
        self.titulo.grid(row=0, column=2, pady=(10,5))
        self.widgets()
    

    def widgets(self):
        self.lbanalisis = tk.Label(root, text="Analisis", font="20")
        self.lbanalisis.grid(row=1, column=0, padx=(10,10), pady=(5,10))

        self.btlexico = tk.Button(root, text="   Lexico   ", command=self.lexico)
        self.btlexico.grid(row=2, column=0)

        self.btsintactico = tk.Button(root, text="Sintactico", command=self.sintactico)
        self.btsintactico.grid(row=3, column=0)

        self.entrada = tk.Text(root, width=50, height=5)
        self.entrada.grid(row=2, column=1, columnspan=3, rowspan=2)

        self.lbresultado = tk.Label(root, text="Resultados", font="20")
        self.lbresultado.grid(row=4, column=0, padx=(10,10), pady=(25,10))

        self.resultados = tk.Text(root, width=50, height=8)
        self.resultados.grid(row=5, column=1, columnspan=3)

        self.btlimpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.btlimpiar.grid(row=5, column=0)

    
    def sintactico(self):
        self.limpiar()
        self.resultados.config(state="normal")
        linea = self.entrada.get(1.0, tk.END) #obtiene el texto de "entrada" 
        if len(linea)==0:
            self.resultados.insert(tk.INSERT, "Inserte una linea de codigo!")
        else:
            result = parser.parse(linea)
            self.resultados.insert(tk.INSERT, result)
        self.resultados.config(state="disable")

    def lexico(self):
        self.limpiar() #vaciar el text
        self.resultados.config(state="normal") #habilitar la escritura en "resultados"
        linea = analizar(self.entrada.get(1.0, tk.END)) #obtiene el texto de "entrada" y analiza su lexico
        if len(linea)==0:
            self.resultados.insert(tk.INSERT, "Inserte una linea de codigo!")
        else: 
            for i in range(len(linea)): #muestra el texto analizado en "resultados"
                self.resultados.insert(tk.INSERT, linea[i])
                self.resultados.insert(tk.INSERT, "\n")
        self.resultados.config(state="disable") #desabilita la escritura en "resultados"
    
    def limpiar(self):
        self.resultados.config(state="normal")
        self.resultados.delete(1.0, tk.END)
        self.resultados.config(state="disable")

#TK ventana principal
root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file='clojure.png'))
root.geometry("600x400")
ventana = Ventana(root)

#inicia el blucle infinito del programa
root.mainloop()
