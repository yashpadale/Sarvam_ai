

import gradio as gr
from RAG import get_answer
from model import call_classification_sarvam
from action import call_action_classification_action_sarvam

import json


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email_function(subject, body, to_email):
    sender_email = "yashpadale108@gmail.com"
    app_password = "ilzs otrh ydjn cwpn"
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, to_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# send_email_function("Hare Krishna","1000","yashpadale108@gmail.com")

def send_email_from_dict(json_string):
    # Parse the JSON string to a dictionary
    email_data = json.loads(json_string)

    # Extract necessary fields
    to_email = email_data.get('email')
    subject = email_data.get('subject')
    content = email_data.get('content')

    # Call the email sending function
    send_email_function(subject, content, to_email)



def perform_operation(json_input):
    # Parse the JSON input
    data = json.loads(json_input)

    # Extract numbers and operation from the JSON data
    numbers = data.get('numbers', [])
    operation = data.get('operation', '')

    # Ensure there are exactly two numbers
    if len(numbers) != 2:
        return "Error: Expected exactly two numbers."

    # Extract the two numbers
    num1, num2 = numbers

    # Perform the operation based on the specified type
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    else:
        return "Error: Unsupported operation."

def process_text(text):
    output=call_classification_sarvam(text)
    print("call_classification_sarvam")
    print(output)
    if output=='RAG':
        prompt, output = get_answer(text)
        print('prompt')
        print(prompt)
        print('output')
        print(output)

        return prompt, output
    if output=='Simple':
        class_=call_action_classification_action_sarvam(text)
        print(class_)
        if class_=='Email':
            text=text+' '+" Give the output in json format such that there are three key value pairs- the email wo whom we have to send and the content of the email and the subject . the key of email should be email and for content should be content , only give the json no other text required. The format should be {'email':'yash@gmail.com','content':'body of the email. ','subject':'The subject of email .'}"
            output=get_model_response(text)

            print('text')
            print(text)
            print('output')
            print(output)
            send_email_from_dict(output)
            return text,output
        if class_=='Simple':
            output=get_model_response(text)
            print('text')
            print(text)
            print('output')
            print(output)
            return text,output
        if class_=='Calculation':
            text=text+' '+" Give the output in json format such that there are two key value pairs- the two numbers we have to operate on and the operation that needs to be done.the key of numbers should be numbers and for operation should be operation only give the json no other text required. The format should be {'numbers' :[ 10 ,12] , 'operation':'+'}  "
            output=get_model_response(text)
            result = perform_operation(output)
            print('text')
            print(text)
            print('output')
            print(output)
            print('result')
            print(result)
            return text,result


# Create the Gradio interface
interface = gr.Interface(
    fn=process_text,  # Function to call
    inputs=gr.Textbox(label="Enter your text"),  # Input component
    outputs=[
        gr.Textbox(label="Prompt When Chunk added"),  # Output component for the prompt
        gr.Textbox(label="Output")   # Output component for the output
    ],
    title="Text Processor",
    description="Enter text to get the prompt and output."
)

# Launch the interface
interface.launch()


#  Explain the concept of transverse wave  .
