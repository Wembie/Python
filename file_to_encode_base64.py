import tkinter as tk
from tkinter import filedialog, messagebox
from base64 import b64encode

def seleccionar_archivo():
    ruta = filedialog.askopenfilename()
    if ruta:
        try:
            with open(ruta, "rb") as archivo:
                codificado = b64encode(archivo.read()).decode()
                texto_resultado.delete("1.0", tk.END)
                texto_resultado.insert(tk.END, codificado)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo codificar el archivo:\n{e}")

def copiar_al_portapapeles():
    resultado = texto_resultado.get("1.0", tk.END).strip()
    if resultado:
        ventana.clipboard_clear()
        ventana.clipboard_append(resultado)
        ventana.update()
        messagebox.showinfo("Copiado", "El texto codificado fue copiado al portapapeles.")
    else:
        messagebox.showwarning("Vacío", "No hay nada que copiar.")

ventana = tk.Tk()
ventana.title("Codificador Base64 de Archivos")
ventana.geometry("800x600")

boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=10)

texto_resultado = tk.Text(ventana, wrap=tk.WORD, height=25)
texto_resultado.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

boton_copiar = tk.Button(ventana, text="Copiar al portapapeles", command=copiar_al_portapapeles)
boton_copiar.pack(pady=10)

ventana.mainloop()
