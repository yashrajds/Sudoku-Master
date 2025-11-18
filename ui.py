import tkinter as tk
from tkinter import messagebox
from sudoku import Sudoku

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Master")
        self.root.geometry("700x850")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # Game variables
        self.levels = {'easy': 5, 'medium': 7, 'hard': 10}
        self.current_level = 'easy'
        self.sudoku = Sudoku(self.levels[self.current_level])
        self.entries = []

        self.create_ui()
        self.new_game()

    # ---------- UI CREATION ----------
    def create_ui(self):
        # Elegant title
        title = tk.Label(
            self.root,
            text="SUDOKU MASTER",
            font=("Segoe UI Black", 32, "bold"),
            fg="#00BFA5",
            bg="#121212"
        )
        title.pack(pady=(10, 10))

        # Subheading
        subtitle = tk.Label(
            self.root,
            text="Sharpen your mind • Solve the puzzle",
            font=("Segoe UI", 13),
            fg="#A0A0A0",
            bg="#121212"
        )
        subtitle.pack(pady=(0, 20))

        # Level selector frame
        level_frame = tk.Frame(self.root, bg="#1E1E1E", bd=0, relief="flat")
        level_frame.pack(pady=(10, 25))

        tk.Label(
            level_frame,
            text="Difficulty:",
            font=("Segoe UI Semibold", 13),
            fg="#FFFFFF",
            bg="#1E1E1E"
        ).pack(side=tk.LEFT, padx=8)

        self.level_var = tk.StringVar(value='easy')
        for level in self.levels:
            rb = tk.Radiobutton(
                level_frame,
                text=level.capitalize(),
                variable=self.level_var,
                value=level,
                command=self.change_level,
                font=("Segoe UI", 12),
                fg="#CCCCCC",
                bg="#1E1E1E",
                selectcolor="#00BFA5",
                activebackground="#1E1E1E",
                activeforeground="#FFFFFF"
            )
            rb.pack(side=tk.LEFT, padx=12)

        # Game board
        self.grid_frame = tk.Frame(self.root, bg="#121212")
        self.grid_frame.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#121212")
        button_frame.pack(pady=25)

        self.new_game_btn = self.create_button(button_frame, "🧩  New Game", "#00BFA5", self.new_game)
        self.new_game_btn.pack(side=tk.LEFT, padx=12)

        self.check_btn = self.create_button(button_frame, "✔️  Check Solution", "#E53935", self.check_solution)
        self.check_btn.pack(side=tk.LEFT, padx=12)

        self.exit_btn = self.create_button(button_frame, "❌  Exit", "#E53935", self.root.destroy)
        self.exit_btn.pack(side=tk.LEFT, padx=12)

        # Footer
        footer = tk.Label(
            self.root,
            text="© 2025 Sudoku Master by YourName",
            font=("Segoe UI", 10),
            fg="#555",
            bg="#121212"
        )
        footer.pack(side=tk.BOTTOM, pady=15)

    # ---------- BUTTON CREATOR ----------
    def create_button(self, parent, text, color, command):
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI Semibold", 13),
            bg=color,
            fg="#FFFFFF",
            activebackground="#FFFFFF",
            activeforeground=color,
            relief="flat",
            bd=0,
            padx=18,
            pady=8,
            command=command
        )
        btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg="#FFFFFF", fg=c))
        btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c, fg="#FFFFFF"))
        return btn

    # ---------- GAME LOGIC ----------
    def change_level(self):
        self.current_level = self.level_var.get()
        self.new_game()

    def new_game(self):
        self.sudoku = Sudoku(self.levels[self.current_level])
        self.sudoku.generate_puzzle(self.current_level)
        self.create_grid()

    def create_grid(self):
        for widget in self.grid_frame.winfo_children(
            
        ):
            widget.destroy()
        self.entries = []

        size = self.levels[self.current_level]
        for i in range(size):
            row = []
            for j in range(size):
                entry = tk.Entry(
                    self.grid_frame,
                    width=3,
                    font=("Consolas", 18, "bold"),
                    justify="center",
                    relief="flat",
                    highlightthickness=1,
                    highlightbackground="#333",
                    highlightcolor="#00BFA5",
                    bg="#1E1E1E",
                    fg="#FFFFFF",
                    insertbackground="#FFFFFF"
                )
                entry.grid(row=i, column=j, padx=2, pady=2, ipadx=2, ipady=2)

                if self.sudoku.board[i][j] != 0:
                    entry.insert(0, str(self.sudoku.board[i][j]))
                    entry.config(state="disabled", disabledbackground="#252525", disabledforeground="#AAAAAA")
                else:
                    entry.bind('<KeyRelease>', lambda e, r=i, c=j: self.validate_input(r, c))

                row.append(entry)
            self.entries.append(row)

    def validate_input(self, row, col):
        entry = self.entries[row][col]
        value = entry.get()
        if value.isdigit():
            num = int(value)
            if 1 <= num <= self.levels[self.current_level]:
                self.sudoku.set_cell(row, col, num)
                entry.config(fg="#00E676")
            else:
                entry.delete(0, tk.END)
        elif value == '':
            self.sudoku.set_cell(row, col, 0)
            entry.config(fg="#FFFFFF")
        else:
            entry.delete(0, tk.END)

    def check_solution(self):
        for i in range(len(self.entries)):
            for j in range(len(self.entries[i])):
                if self.entries[i][j]['state'] != 'disabled':
                    value = self.entries[i][j].get()
                    self.sudoku.set_cell(i, j, int(value) if value.isdigit() else 0)

        if self.sudoku.check_solution():
            messagebox.showinfo("Sudoku Master", "🎉 Excellent! You solved the puzzle.")
        else:
            messagebox.showerror("Sudoku Master", "❌ Not quite right. Try again!")

# ---------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
