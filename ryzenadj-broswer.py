import tkinter as tk
import os, subprocess

PATH = "C:/MyScripts/ryzenadj"
scripts = os.listdir(PATH)

root = tk.Tk()
root.title('Ryzenadj Runner')
root.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + '/' + 'ryzen-logo.ico')
root.geometry("520x540")

script_listbox = tk.Listbox(root, width=40)
script_listbox.pack(pady=15)

for script in scripts:
    script_listbox.insert("end", script)

def run():
    script = script_listbox.get("anchor")
    output_text.delete(1.0,"end")
    cmd = os.path.join(PATH, script)
    output = subprocess.getoutput(cmd)
    output_text.config(state='normal')
    output_text.insert("end", output)
    output_text.config(state='disabled')

run_button = tk.Button(root, text="Run", command=run)
run_button.pack(pady=10)

output_label = tk.Label(root, text="Output:")
output_label.pack(pady=5)

output_text = tk.Text(root, width=50, height=15)
output_text.config(state='disabled')
output_text.pack(pady=5)

root.mainloop()