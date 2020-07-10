import sys
import json
import re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def create_intents(file_contents):

    # Split transcript by newlines
    split_lines = file_contents.split('\n')
    lines_without_speaker = []
    lines_with_context = []

    # Go through each line
    for line in split_lines:
        # Remove the speaker
        lines_without_speaker.append(line.split(':')[1])

        # Strip whitespace
        lines_without_speaker[-1] = lines_without_speaker[-1].strip()

        # Here we create the dictionary entry that will be added to the json
        if len(lines_without_speaker) > 1:
            lines_with_context.append({
                "line": lines_without_speaker[-1],
                "previous line": lines_without_speaker[-2]
            })
        else:
            lines_with_context.append({
                "line": lines_without_speaker[-1],
                "previous line": "NO PREVIOUS LINE"
            })
    # Depending on whether the JSON file exists we will either want to read it or create a new one
    try:
        json_file = open('./json.txt', 'r+')
    except FileNotFoundError:
        print("No json file currently exists, creating one now.")
        json_file = open('./json.txt', 'w+')

    json_file_contents = json_file.read()
    json_file.close()
    new_json_file = open('./json.txt', 'w+')
    print("JSON file contents is: " + json_file_contents)
    if not json_file_contents:
        new_json = json.dumps(lines_with_context)
        new_json_file.write(new_json)
    else:
        current_json = json.loads(json_file_contents)
        new_json = current_json
        for line in lines_with_context:
            new_json.append(line)
        string_json = json.dumps(new_json)
        new_json_file.write(string_json)
    new_json_file.close()
    sys.exit()



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.file_dialog()

    def file_dialog(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.ExistingFile)
        name = QFileDialog.getOpenFileName(self, 'Open File')
        file_contents = open(name[0]).read()
        print(file_contents)
        create_intents(file_contents)


def main():
    app = QApplication(sys.argv)
    fd = App()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
