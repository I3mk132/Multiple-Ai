import customtkinter as ctk
from gemini import *
class App(ctk.CTk):
    def __init__(self, WIDTH, HEIGHT, main_color="blue", main_font="segoe print"):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.main_color = main_color
        self.main_font = main_font
        self.v = 0
        super().__init__()
        # ======================= window settings =======================
        # root = ctk.CTk()
        self.title("chatbot")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False,False)
        # ================================ frames ====================================
        self.top_frame = ctk.CTkFrame(
            master=self,
            width=self.WIDTH,
            height=(self.HEIGHT*(1/12)),
            border_width=2,
            border_color='gray'
        )
        self.top_frame.pack()

        self.body_frame = ctk.CTkScrollableFrame(
            master=self,
            width=self.WIDTH,
            height=(self.HEIGHT*(9/12)),
            border_width=2,
            border_color='gray'
        )
        self.body_frame.pack()

        self.buttom_frame = ctk.CTkFrame(
            master=self,
            width=self.WIDTH,
            height=(self.HEIGHT*(2/12)),
            border_width=2,
            border_color='gray'
        )
        self.buttom_frame.pack()
        # ================================ widgets ====================================
        self.quit_button = ctk.CTkButton(
            master=self.top_frame,
            text="Quit",
            width=(self.WIDTH*(1/12)),
            height=(self.HEIGHT*(1/12)),
            fg_color='red',
            border_color='gray',
            corner_radius=50,
            font=(self.main_font, 16),
            command=self.close_app
        )
        self.quit_button.pack(side='left')

        self.choose_path_combobox = ctk.CTkComboBox(
            master=self.top_frame,
            width=(self.WIDTH*(5/12)),
            height=(self.HEIGHT*(1/12)),
            corner_radius=50,
            font=(self.main_font, 16),
            values=['new', 'old'],
            state='readonly'
        )
        self.choose_path_combobox.pack(side='left')

        self.options_ai_combobox = ctk.CTkComboBox(
            master=self.top_frame,
            width=(self.WIDTH*(4/12)),
            height=(self.HEIGHT*(1/12)),
            corner_radius=50,
            font=(self.main_font, 16),
            values=['chat-gpt', 'gemini'],
            state='readonly',
            hover=True
        )
        self.options_ai_combobox.pack(side='left')

        self.bot_confirm_button = ctk.CTkButton(
            master=self.top_frame,
            text="✓",
            width=(self.WIDTH*(2/12)),
            height=(self.HEIGHT*(1/12)),
            corner_radius=50,
            font=(self.main_color,16),
            command=self.on_top_button_clicked
        )
        self.bot_confirm_button.pack(side='left')

       # body widgets ####################################


       ###################################################
        self.user_input_massage = ctk.CTkTextbox(
            master=self.buttom_frame,
            width=(self.WIDTH*(10/12)),
            height=(self.HEIGHT*(9/12)),
            font=(self.main_font, 16)
        )
        self.user_input_massage.pack(side='left')

        self.user_input_send_button = ctk.CTkButton(
            master=self.buttom_frame,
            text="✓",
            width=(self.WIDTH*(2/12)),
            height=(self.HEIGHT*(2/12)),
            corner_radius=50,
            font=(self.main_font, 16),
            command=self.on_enter
        )
        self.user_input_send_button.pack(side='left')

        # =================== keyboard bindings ===========================
        self.user_input_massage.bind("<Shift-Return>", self.on_shift_enter)
        self.user_input_massage.bind("<Return>" , self.on_enter)
        self.user_input_massage.bind("<Return>", lambda event: "break")
        self.user_input_massage.bind("<Control-BackSpace>", self.on_ctrl_backspace)

    # =========================== methods =========================
    def close_app(self):
        self.quit()
    

    def on_shift_enter(self, event):
        self.user_input_massage.insert(ctk.END, '\n')
        return "break"  # Ignore Enter key press

    def on_ctrl_backspace(self, event):
        self.user_input_massage.delete("1.0", ctk.END)
        return "break"
    

    def on_enter(self,event=None):
        user_input_var = self.user_input_massage.get("1.0", ctk.END)
        print(user_input_var)

        self.user_input_massage.delete("1.0", ctk.END)
        # where the input will go
        question, answer = conversation_loop(user_input_var, new, chat, time, old_chat_path)
        ctk.CTkLabel(
            master=self.body_frame,
            text="YOU> "+ question,
            font=(self.main_font, 16),
            wraplength=600
        ).grid(row=self.v*2, column=0, sticky=ctk.W)
        ctk.CTkLabel(
            master=self.body_frame,
            text="CHATBOT> "+ answer,
            font=(self.main_font, 16),
            wraplength=600
        ).grid(row=self.v*2+1, column=0, sticky=ctk.W)

        self.v += 1
        

    def on_top_button_clicked(self):
        global new, old_chat_path, chat, time
        old_or_new = self.choose_path_combobox.get()
        choosed_ai = self.options_ai_combobox.get()
        if choosed_ai == 'gemini':
            if old_or_new == "new":
                #call func
                history, new = new_chat()
                old_chat_path = None

            else:
                history, new, old_chat_path = old_chat()

            chat, time = start_conversation(history)
            
        else:
            print('coming soon!!')