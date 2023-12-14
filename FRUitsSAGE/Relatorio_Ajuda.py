import tkinter as tk

class VisualizadorArquivoTexto:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AJUDA??")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.texto = tk.Text(self.frame, wrap="word", width=60, height=20)
        self.texto.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self.frame, command=self.texto.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.texto.config(yscrollcommand=self.scrollbar.set)

        
        self.abrir_arquivo("./arquivo/Relatório.txt")
        self.root.mainloop()
    def abrir_arquivo(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.texto.delete("1.0", tk.END)  # Limpar qualquer conteúdo anterior
                self.texto.insert(tk.END, conteudo)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {file_path}")



app = VisualizadorArquivoTexto

