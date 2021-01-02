from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
     return render_template("index.html")

@app.route('/video',methods=['GET','POST'])
def video():
    if request.method == 'POST':
        url = request.form.get('url')
    else:
        url = request.args.get('url')

    return render_template("video.html", url = url)




if __name__ == '__main__':
    app.run(host="0.0.0.0",port= 5000)
