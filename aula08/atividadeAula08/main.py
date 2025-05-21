import tkinter as tk
from tkinter import messagebox
from Categoria import Categoria
from Desktop import Desktop
from Notebook import Notebook

class AppProdutos:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Produtos")
        
        # Categoria fixa (simplificação)
        self.categoria = Categoria(1, "Informática")
        
        # Widgets
        self.criar_widgets()
    
    def criar_widgets(self):
        # Label para Modelo
        tk.Label(self.janela, text="Modelo:").pack()
        self.entry_modelo = tk.Entry(self.janela)
        self.entry_modelo.pack()
        
        # Label para Cor
        tk.Label(self.janela, text="Cor:").pack()
        self.entry_cor = tk.Entry(self.janela)
        self.entry_cor.pack()
        
        # Label para Preço
        tk.Label(self.janela, text="Preço (R$):").pack()
        self.entry_preco = tk.Entry(self.janela)
        self.entry_preco.pack()
        
        # Label para Tipo
        tk.Label(self.janela, text="Tipo:").pack()
        self.tipo_var = tk.StringVar(value="Desktop")
        tk.Radiobutton(self.janela, text="Desktop", variable=self.tipo_var, value="Desktop", command=self.mostrar_campo).pack()
        tk.Radiobutton(self.janela, text="Notebook", variable=self.tipo_var, value="Notebook", command=self.mostrar_campo).pack()
        
        self.frame_detalhes = tk.Frame(self.janela)
        self.frame_detalhes.pack()
        self.mostrar_campo()
        
        tk.Button(self.janela, text="Cadastrar", command=self.cadastrar).pack(pady=10)
    
    def mostrar_campo(self):
        for widget in self.frame_detalhes.winfo_children():
            widget.destroy()
        
        tipo = self.tipo_var.get()
        label_texto = "Potência da Fonte (W):" if tipo == "Desktop" else "Tempo de Bateria (h):"
        
        tk.Label(self.frame_detalhes, text=label_texto).pack()
        self.entry_detalhe = tk.Entry(self.frame_detalhes)
        self.entry_detalhe.pack()
    
    def cadastrar(self):
        modelo = self.entry_modelo.get()
        cor = self.entry_cor.get()
        preco = float(self.entry_preco.get())
        tipo = self.tipo_var.get()
        detalhe = float(self.entry_detalhe.get())
            
        if not modelo or not cor:
            raise ValueError("Preencha modelo e cor!")
            
        if tipo == "Desktop":
            produto = Desktop(modelo, cor, preco, self.categoria, detalhe)
        else:
            produto = Notebook(modelo, cor, preco, self.categoria, detalhe)
            
        produto.cadastrar()
            
        info = produto.getInformacoes()
        mensagem = (
            f"Modelo: {info['modelo']}\n"
            f"Cor: {info['cor']}\n"
            f"Preço: R${info['preco']}\n"
            f"Categoria: {info['categoria'][1]}\n"
            f"Detalhe: {detalhe} {'W' if tipo == 'Desktop' else 'h'}"
        )
            
        messagebox.showinfo("Sucesso", f"{tipo} cadastrado!\n{mensagem}")
        
        # Pra limar, caso contrario iria ficar preenchido com o último cadastro
        self.entry_modelo.delete(0, tk.END)
        self.entry_cor.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_detalhe.delete(0, tk.END)
        
app = AppProdutos()
app.janela.mainloop()