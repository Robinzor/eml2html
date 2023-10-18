import argparse
import os
from extract_msg import Message

def convert_msg_to_html(msg_file_path):
    # Get the path to the .msg file
    msg = Message(msg_file_path)
    msg.save(html=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .msg to .html and .pdf")
    parser.add_argument("input_msg", help="Path to the .msg file")
    args = parser.parse_args()
    input_msg = args.input_msg

    convert_msg_to_html(input_msg)

# Usage py .\main.py test.msg