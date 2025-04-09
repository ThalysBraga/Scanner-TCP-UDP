import socket
import customtkinter as ctk
from tkinter import messagebox, filedialog

def scan_tcp(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        return "Aberta"
    except socket.timeout:
        return "Filtrada (sem resposta)"
    except socket.error:
        return "Fechada ou Filtrada"

def scan_udp(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    try:
        s.sendto(b'', (ip, port))
        data, _ = s.recvfrom(1024)
        s.close()
        return "Aberta"
    except socket.timeout:
        return "Aberta ou Filtrada (sem resposta)"
    except socket.error:
        return "Fechada"

def start_scan():
    ip = ip_entry.get()
    ports_text = ports_entry.get()
    try:
        socket.inet_aton(ip)
    except socket.error:
        messagebox.showerror("Erro", "Endereço IP inválido.")
        return

    try:
        ports = [int(p.strip()) for p in ports_text.split(',')]
    except ValueError:
        messagebox.showerror("Erro", "Portas inválidas. Use formato como: 22,80,443")
        return

    result_box.configure(state="normal")
    result_box.delete("1.0", "end")

    report_lines = []
    report_lines.append(f"Varredura de portas TCP em {ip}:\n")
    for port in ports:
        status = scan_tcp(ip, port)
        line = f"  Porta TCP {port}: {status}"
        result_box.insert("end", line + "\n")
        report_lines.append(line)

    report_lines.append(f"\nVarredura de portas UDP em {ip}:\n")
    for port in ports:
        status = scan_udp(ip, port)
        line = f"  Porta UDP {port}: {status}"
        result_box.insert("end", line + "\n")
        report_lines.append(line)

    result_box.configure(state="disabled")

    global last_report  # Armazena resultado para exportação
    last_report = "\n".join(report_lines)

def export_report():
    if not last_report:
        messagebox.showinfo("Aviso", "Nenhum resultado para exportar.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os arquivos", "*.*")]
    )
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(last_report)
        messagebox.showinfo("Sucesso", f"Relatório exportado para:\n{filepath}")

# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.title("Scanner de Portas TCP/UDP")
root.geometry("600x600")

last_report = ""  # Resultado do scan para exportação

# Frame principal
frame = ctk.CTkFrame(master=root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# IP
ip_label = ctk.CTkLabel(master=frame, text="Endereço IP:")
ip_label.pack(pady=(10, 5))
ip_entry = ctk.CTkEntry(master=frame, width=400)
ip_entry.pack()

# Portas
ports_label = ctk.CTkLabel(master=frame, text="Portas (separadas por vírgula):")
ports_label.pack(pady=(15, 5))
ports_entry = ctk.CTkEntry(master=frame, width=400)
ports_entry.insert(0, "22,53,80,139,445,330")
ports_entry.pack()

# Botões
button_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
button_frame.pack(pady=20)

scan_button = ctk.CTkButton(master=button_frame, text="Iniciar Varredura", command=start_scan)
scan_button.pack(side="left", padx=10)

export_button = ctk.CTkButton(master=button_frame, text="Exportar Relatório", command=export_report)
export_button.pack(side="left", padx=10)

# Resultado
result_box = ctk.CTkTextbox(master=frame, width=520, height=250)
result_box.pack(pady=10)
result_box.configure(state="disabled")

root.mainloop()
