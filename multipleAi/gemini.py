import google.generativeai as genai
from dotenv import load_dotenv
import os
import datetime
from tkinter import filedialog
import tkinter as tk
import json

# functions
def read_file_lines(file_path=None):  # reading the old chat files and adding it into a list
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(data)
    return data

def save_chat_into_file(question, answer, saving_file_text):  # writing the chat into the text file
    file_path = saving_file_text
    with open(file_path, 'r') as file:
        chat_data = json.load(file)

    new_user_question = {
        "role":"user",
        "parts":question
    }
    new_system_answer = {
        "role":"model",
        "parts":answer   
    }
    chat_data.append(new_user_question)
    chat_data.append(new_system_answer)

    with open(file_path, 'w') as file:
        json.dump(chat_data, file, indent=2)

    print(f"Data inserted into {file_path}")

def get_chosen_path():  # getting the old file path  from the user
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title='Select a json file', filetypes=[("json files", "*.json")])
    if file_path:
        print("selected file path: " + file_path)
        return file_path
    root.mainloop()

# tkinter window for the filedialog


def get_the_time():
    # current time is : 
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%Y-%m-%d_%H-%M_")
    print(current_time_str)
    return current_time_str

def get_api_configs():
    # set the genai configurations
    load_dotenv()
    API_KEY = os.getenv('GEMINI_API_KEY')   
    genai.configure(api_key=API_KEY)

    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    ]
    return generation_config, safety_settings

# check for existing chat
def new_chat():
    
    history = []
    new = True
    return history, new


def old_chat():
    new = False
    old_chat_path = get_chosen_path()
    continue_chat = read_file_lines(old_chat_path)
    if continue_chat == [None]:
        print('the list is empty')
        continue_chat = []
    history = continue_chat
    return history, new, old_chat_path


def start_conversation(history):
    generation_config, safety_settings = get_api_configs()
    time = get_the_time()
    print(history)
    # starting the chat
    model = genai.GenerativeModel('gemini-1.0-pro',
                                generation_config=generation_config,
                                safety_settings=safety_settings,
                                )
    chat = model.start_chat(history=history)
    print("Hi there! I am Gemini! How can i Help You?")
    return chat, time

def conversation_loop(user_input, new, chat, time, old_chat_path):
    
    # conversation loop
    question = user_input

    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')
    if new:
        the_new_saving_text_file = f'saved_chats/saved_chat {time}.json'
        if os.path.exists(the_new_saving_text_file):
                pass
        else:
            with open(the_new_saving_text_file, 'w') as file:
                json.dump([], file)
    else:
        the_new_saving_text_file = old_chat_path
        
    save_chat_into_file(question, response.text, the_new_saving_text_file)  # sending to writing function
    return question, response.text