from characterai import PyCAI
from dotenv import load_dotenv
import os

load_dotenv()
client = PyCAI(os.getenv('CAI_TOKEN'))

char = input('Enter CHAR: ')

chat = client.chat.get_chat(char)

participants = chat['participants']

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

while True:
    message = input('You: ')

    data = client.chat.send_message(
        chat['external_id'], tgt, message
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    print(f"{name}: {text}")