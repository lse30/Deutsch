import tkinter as tk
from tkinter import END
from leitner_system import LeitnerSystem, WordData
from styles import StyleProfile
from meta_data import word_files


class FlashCard:
    def __init__(self):
        self.system = None
        self.files = None
        self.fail_state = False
        self.style = StyleProfile(True)
        self.root = tk.Tk()
        self.root.config(bg=self.style.background)
        self.root.title("Flashcard")

        self.flash_card, self.counter, self.result = self.draw_top_frame()
        self.entry_box, self.start_button, self.end_button, self.select_button = self.draw_bottom_frame()

    def draw_top_frame(self):
        top_frame = tk.Frame(self.root, bg=self.style.background)
        top_frame.pack(fill=tk.X)

        for i in range(2):
            top_frame.rowconfigure(i, weight=1, minsize=50)
            for j in range(3):
                top_frame.columnconfigure(j, weight=1, minsize=75)

        category_frame = tk.Frame(
            master=top_frame,
            borderwidth=3,
            relief=tk.GROOVE,
            bg=self.style.primary
        )
        category_frame.grid(row=0, column=0)
        category = tk.Label(
            master=category_frame,
            width=30,
            text="0/0",
            font=self.style.standard_font,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        category.pack()

        result_frame = tk.Frame(
            master=top_frame,
            borderwidth=3,
            relief=tk.GROOVE,
            bg=self.style.primary
        )
        result_frame.grid(row=0, column=2)
        result = tk.Label(
            master=result_frame,
            width=30, text="",
            font=self.style.standard_font,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        result.pack()

        flashcard_frame = tk.Frame(
            master=top_frame,
            relief=tk.RAISED,
            bg=self.style.primary,
            borderwidth=5,
        )
        flashcard_frame.grid(
            row=1,
            column=0,
            columnspan=3,
            padx=5,
            pady=(5, 15)
        )
        flashcard = tk.Label(
            master=flashcard_frame,
            width=55, height=8,
            text="Select Files",
            font=self.style.flash_font,
            bg=self.style.surface,
            fg=self.style.secondary
        )
        flashcard.pack()

        return flashcard, category, result

    def draw_bottom_frame(self):
        bottom_frame = tk.Frame(self.root, bg=self.style.background)
        bottom_frame.pack(fill=tk.X)

        for i in range(2):
            bottom_frame.rowconfigure(i, weight=1, minsize=50)
            for j in range(9):
                bottom_frame.columnconfigure(j, weight=1, minsize=50)

        entry_frame = tk.Frame(
            master=bottom_frame,
            borderwidth=3,
            relief=tk.GROOVE,
            bg=self.style.on_surface
        )
        entry_frame.grid(row=0, column=0, columnspan=4)
        entry_box = tk.Entry(
            master=entry_frame,
            width=44,
            font=self.style.standard_font,
            bg=self.style.entry_background,
            fg=self.style.on_secondary
        )
        entry_box.bind("<Return>", self.on_entry_submit)
        entry_box.pack()

        for i, x in enumerate(['ü', 'ä', 'ö', 'ß']):
            button_frame = tk.Frame(
                master=bottom_frame,
                relief=tk.RAISED,
                bg=self.style.on_surface,
                borderwidth=1
            )
            button_frame.grid(row=0, column=(i + 4))
            button = tk.Button(
                master=button_frame,
                font=self.style.standard_font,
                text=x,
                command=lambda x=x: self.add_character(x),
                width=3,
                bg=self.style.surface,
                fg=self.style.on_surface
            )
            button.pack()

        button_frame = tk.Frame(
            master=bottom_frame,
            relief=tk.RAISED,
            bg=self.style.on_surface,
            borderwidth=1
        )
        button_frame.grid(row=0, column=8)
        sound_button = tk.Button(
            master=button_frame,
            font=self.style.standard_font,
            text='play',
            command=self.play_word,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        sound_button.pack()

        start_frame = tk.Frame(
            master=bottom_frame,
            relief=tk.RAISED,
            bg=self.style.on_surface,
            borderwidth=1
        )
        start_frame.grid(row=1, column=0, columnspan=2)
        start_button = tk.Button(
            master=start_frame,
            width=30,
            height=2,
            text="Start",
            command=self.start_session,
            font=self.style.standard_font,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        start_button.pack()

        end_frame = tk.Frame(
            master=bottom_frame,
            relief=tk.RAISED,
            borderwidth=1,
            bg=self.style.on_surface
        )
        end_frame.grid(row=1, column=2, columnspan=2)
        end_button = tk.Button(
            master=end_frame,
            width=30,
            height=2,
            text="End",
            command=self.end_session,
            font=self.style.standard_font,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        end_button.pack()

        select_frame = tk.Frame(
            master=bottom_frame,
            relief=tk.RAISED,
            borderwidth=1,
            bg=self.style.on_surface
        )
        select_frame.grid(row=1, column=4, columnspan=5)
        select_button = tk.Button(
            master=select_frame,
            width=60,
            height=2,
            text=f"Select Files",
            command=self.open_popup,
            font=self.style.standard_font,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        select_button.pack()
        return entry_box, start_button, end_button, select_button

    def open_popup(self):

        def on_checkbox_clicked(checkbox_name, var):
            if var.get():
                print(f"{checkbox_name} checkbox is checked")
            else:
                print(f"{checkbox_name} checkbox is unchecked")

        def select_all_checkboxes(checkbox_state):
            for var in checkbox_state:
                var.set(1)

        def submit_selection():
            output = [word_files[x][1] for x, var in enumerate(checkbox_vars) if var.get() == 1]
            print(output)
            top.destroy()
            self.files = output

        top = tk.Toplevel(self.root)
        top.title("Select Files")
        top.config(bg=self.style.background)
        title = tk.Label(
            top,
            text='Select Files',
            font=self.style.standard_font,
            bg=self.style.background,
            fg=self.style.on_background,
            pady=5,
            padx=5
        )
        title.pack()
        checkbox_frame = tk.Frame(
            master=top,
            borderwidth=3,
            relief=tk.GROOVE,
            bg=self.style.surface,
            pady=5,
            padx=5
        )
        checkbox_frame.pack()

        checkbox_vars = [tk.IntVar() for _ in range(len(word_files))]

        for i, filename in enumerate(word_files):
            checkbox = tk.Checkbutton(
                checkbox_frame,
                text=filename[0],
                variable=checkbox_vars[i],
                font=self.style.standard_font,
                command=lambda i=i: on_checkbox_clicked(word_files[i][0], checkbox_vars[i]),
                bg=self.style.surface,
                fg=self.style.on_surface

            )
            checkbox.grid(row=i, column=0, sticky=tk.W)

        button_frame = tk.Frame(
            master=top,
            borderwidth=3,
            relief=tk.GROOVE,
            bg=self.style.primary
        )
        button_frame.pack()
        all_button = tk.Button(
            master=button_frame,
            width=10,
            height=1,
            text="All",
            font=self.style.standard_font,
            command=lambda: select_all_checkboxes(checkbox_vars),
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        all_button.grid(row=0, column=0)
        ok_button = tk.Button(
            master=button_frame,
            width=10,
            height=1,
            text="Ok",
            font=self.style.standard_font,
            command=submit_selection,
            bg=self.style.surface,
            fg=self.style.on_surface
        )
        ok_button.grid(row=0, column=1)

    def start_session(self):
        if self.system:
            self.system.update_words()
        if not self.files:
            self.files = [x[1] for x in word_files]
        self.system = LeitnerSystem(*self.files)
        self.on_button_click()

    def on_button_click(self):
        word: WordData = self.system.serve_word()
        if word:

            print(word.category)
            self.flash_card.config(
                text=word.get_next_prompt(),
                bg=self.style.surface,
                fg=self.style.secondary
            )
            self.counter.config(text=self.system.get_counter())
            self.play_word()
        else:

            self.counter.config(text=self.system.get_counter())
            promoted = self.system.update_words()
            self.flash_card.config(
                text=f"END OF WORDLIST - {promoted} words promoted",
                bg=self.style.success_green,
                fg=self.style.on_background
            )
            self.system = None

    def end_session(self):
        if self.system:
            self.system.update_words()
            self.flash_card.config(text="Press Start", bg=self.style.surface, fg=self.style.on_background)
            self.system = None
        self.root.destroy()

    def on_entry_submit(self, _args):
        answer = self.entry_box.get()
        if self.fail_state:
            result = self.system.is_answer_correct(answer)
        else:
            result = self.system.submit_answer(answer)

        print(f"you guessed [{answer}]")
        print(self.system.current_word)

        if result:
            print('Correct!')
            self.fail_state = False
            self.result.config(
                text=self.system.get_answer(),
                background=self.style.success_green,
                fg=self.style.result_text
            )
            self.on_button_click()
        else:
            print("Fail!")
            self.fail_state = True
            self.result.config(
                text=f"{self.system.get_answer()}\nYou Guessed: {answer}",
                background=self.style.failure_red,
                fg=self.style.result_text
            )
            self.flash_card.config(text=self.system.get_answer(), background=self.style.failure_red,
                                   fg=self.style.result_text)

        self.entry_box.delete(0, END)

    def add_character(self, char_to_add):
        if len(self.entry_box.get()) == 0:
            char_to_add = char_to_add.upper()
        self.entry_box.insert(END, char_to_add)

    def play_word(self):
        if self.system:
            if self.system.current_word:
                current_prompt = self.system.current_word.current_prompt
                if current_prompt == 'g' or self.fail_state:
                    self.system.play_word()
                    return
                else:
                    return
        print("system unavailable to play sound")

    def run(self):
        self.root.mainloop()


# Create and run the application
app = FlashCard()
app.run()
