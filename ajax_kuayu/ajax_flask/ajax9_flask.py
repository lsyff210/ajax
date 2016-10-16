from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('jsonp.html',)


@app.route('/tvList')
def tvList():
    return render_template('list.html',)

if __name__ == '__main__':
    app.run(debug=True, extra_files=[os.path.join(app.root_path, app.template_folder)])
