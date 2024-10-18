from flask import*
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')
def login():
    username=request.form GET ['username']
    password=request.form GET ['password']
    if username=="juraij"and password=="jinn":
        return "welcome %s"%username

if __name__=='__main__':
    app.run(debug=True)