import os
from flask import Flask, render_template

base_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(base_dir)
project_dir = os.path.join(base_dir, 'testProject/')
template_dir = os.path.join(project_dir, 'templates/html')
print('temp' + template_dir)

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    return 'Test Address Hello World!!!'

@app.route('/main2')
def main2():
    return 'Test Address Hello World!!!!!!~~~~ HI.!!!!'

@app.route('/test')
def test():
    return render_template('main.html')

if __name__ == "__main__":
    print("server is running on localhost!!")
    app.run(host='0.0.0.0', port=8888, debug=False)