import tkinter as tk
from tkinter import messagebox

class CandidateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список кандидатов")

        self.candidates = []

        self.label = tk.Label(root, text="Имя кандидата:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Добавить кандидата", command=self.add_candidate)
        self.add_button.pack(pady=10)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Удалить выбранного кандидата", command=self.remove_candidate)
        self.remove_button.pack(pady=10)

    def add_candidate(self):
        candidate_name = self.entry.get().strip()
        if candidate_name:
            self.candidates.append(candidate_name)
            self.listbox.insert(tk.END, candidate_name)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Внимание", "Введите имя кандидата")

    def remove_candidate(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_candidate = self.candidates.pop(index)
            self.listbox.delete(index)
            messagebox.showinfo("Успех", f"Кандидат {removed_candidate} удален")
        else:
            messagebox.showwarning("Внимание", "Выберите кандидата для удаления")

if __name__ == "__main__":
    root = tk.Tk()
    app = CandidateApp(root)
    root.mainloop()
