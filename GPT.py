import cv2
import pytesseract
import tkinter as tk
import openai
import os
from dotenv import load_dotenv
from tkinter import filedialog

load_dotenv()
openai.api_key = openAiKey= os.environ.get('OPENAI_KEY')
model_id = 'gpt-3.5-turbo'


# Define a function to generate the response
def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


# Define a function to upload the image and generate the response
def upload_image_and_generate_response():
    # Prompt the user to select an image file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    
    # Load the image
    img = cv2.imread(file_path)
    
    # Extract the text from the image
    text = pytesseract.image_to_string(img)

    conversation = []
    conversation.append({'role': 'system', 'content': f'{text}'})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    # Display the generated response
    
# Create a GUI window
window = tk.Tk()
window.title('Image Recognition App')

# Create a button to upload the image and generate the response
button = tk.Button(window, text='Upload Image', command=upload_image_and_generate_response)
button.pack(pady=10)

# Create a label to display the generated response
response_label = tk.Label(window, text='')
response_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
