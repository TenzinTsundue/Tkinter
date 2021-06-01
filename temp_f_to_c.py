import tkinter as tk 

def convert():
	fahrenheit = ent_temperature.get()         #get value from entry
	celsius = (float(fahrenheit) - 32) * (5/9)
	lbl_result["text"] = f"{round(celsius, 2)}\N{DEGREE CELSIUS}"    #put result in label text

window = tk.Tk()
window.title("Temperature Converter")      #title of program

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_tmp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_tmp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
	master=window,
	text="\N{RIGHTWARDS BLACK ARROW}",
	command=convert
	)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()