import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x500")

        self.equation = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row_val, column=col_val)

    def click_event(self, key):
        current_equation = self.equation.get()
        
        if key == '=':
            try:
                result = str(eval(current_equation))
                self.equation.set(result)
            except Exception as e:
                self.equation.set('Error')
        else:
            self.equation.set(current_equation + key)

    def clear(self):
        self.equation.set('')

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
