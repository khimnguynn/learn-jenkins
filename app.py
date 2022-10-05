from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
   return render_template('index.html')
@app.route('/')
def index():
   return "HOME PAGE"


if __name__ == '__main__':
   app.run("0.0.0.0", port=8080)