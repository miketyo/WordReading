from flask import Flask, render_template, request
import random
import time, os

app = Flask(__name__)

words_folder = 'words'
word_files = [file.replace('.txt','') for file in os.listdir(words_folder) if file.endswith('.txt')]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_file = request.form['file']
        level = int(request.form['level'])
        word = get_random_word(selected_file)
        display_time = get_display_time(level)

        return render_template('index.html', word=word, display_time=display_time, files=word_files, selected_file=selected_file, level=level)

    return render_template('index.html', files=word_files)


def get_random_word(file_name):
    file_path = os.path.join(words_folder, file_name+'.txt')
    with open(file_path, 'r') as file:
        word_list = [line.strip() for line in file]
    return random.choice(word_list)

def get_display_time(level):
    time_mapping = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2}
    return time_mapping.get(level, 6)  # Default to 5 seconds if an invalid level is provided

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
