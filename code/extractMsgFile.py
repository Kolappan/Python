import os
from extract_msg import Message

def msg_to_txt(input_file, output_file):
    # Load the .msg file
    msg = Message(input_file)

    # Extract the email body
    body = msg.body

    # Save the body to a .txt file
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(body)

    print(f'Successfully saved email body from {input_file} to: {output_file}')

def process_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_name in os.listdir(input_directory):
        if file_name.endswith('.msg'):
            input_file = os.path.join(input_directory, file_name)
            output_file = os.path.join(output_directory, file_name.replace('.msg', '.txt'))
            msg_to_txt(input_file, output_file)

# Replace these with your input and output directory paths
# Replace these with your .msg and .txt file paths
input_directory = 'msgFiles'
output_directory = 'outText'

process_directory(input_directory, output_directory)

