import tkinter as tk

def result():
	calculation = ent_val.get()
	lbl_result["text"] = eval(calculation)

def entry(btn):
	ent_val.insert("end", btn["text"])

def clear():
	ent_val.delete(0, "end")
	lbl_result["text"] = ""

window = tk.Tk()
window.title("Calculator")

ent_val = tk.Entry(master=window, width=32)
lbl_result =tk.Label(master=window, width=10)
btn_clear = tk.Button(master=window, text="Clear", width=28, command=clear)

frm_btn = tk.Frame(master=window)
frm_btn.rowconfigure([0, 1, 2, 3], minsize = 50)
frm_btn.columnconfigure([0, 1, 2, 3], minsize = 50)

btn_1 = tk.Button(master=frm_btn, text ="1", command=lambda: entry(btn_1))
btn_2 = tk.Button(master=frm_btn, text ="2", command=lambda: entry(btn_2))
btn_3 = tk.Button(master=frm_btn, text ="3", command=lambda: entry(btn_3))
btn_add = tk.Button(master=frm_btn, text ="+", command=lambda: entry(btn_add))

btn_4 = tk.Button(master=frm_btn, text ="4", command=lambda: entry(btn_4))
btn_5 = tk.Button(master=frm_btn, text ="5", command=lambda: entry(btn_5))
btn_6 = tk.Button(master=frm_btn, text ="6", command=lambda: entry(btn_6))
btn_sub = tk.Button(master=frm_btn, text ="-", command=lambda: entry(btn_sub))

btn_7 = tk.Button(master=frm_btn, text ="7", command=lambda: entry(btn_7))
btn_8 = tk.Button(master=frm_btn, text ="8", command=lambda: entry(btn_8))
btn_9 = tk.Button(master=frm_btn, text ="9", command=lambda: entry(btn_9))
btn_mult = tk.Button(master=frm_btn, text ="*", command=lambda: entry(btn_mult))

btn_0 = tk.Button(master=frm_btn, text ="0", command=lambda: entry(btn_0))
btn_pt = tk.Button(master=frm_btn, text =".", command=lambda: entry(btn_pt))
btn_eql= tk.Button(master=frm_btn, text ="=", command=result)
btn_div= tk.Button(master=frm_btn, text ="/", command=lambda: entry(btn_div))


ent_val.grid(row=0, column=0, pady=5)
lbl_result.grid(row=1, column=0)
frm_btn.grid(row=2, column=0)
btn_clear.grid(row=3, column=0)

btn_1.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
btn_2.grid(row=0, column=1, sticky="nsew", padx=1, pady=1)
btn_3.grid(row=0, column=2, sticky="nsew", padx=1, pady=1)
btn_add.grid(row=0, column=3, sticky="nsew", padx=1, pady=1)

btn_4.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
btn_5.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
btn_6.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
btn_sub.grid(row=1, column=3, sticky="nsew", padx=1, pady=1)

btn_7.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
btn_8.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
btn_9.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
btn_mult.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

btn_0.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)
btn_pt.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
btn_eql.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)
btn_div.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)



window.mainloop()