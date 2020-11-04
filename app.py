from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c26619b3d776b24c12406d8b7c167d67'

posts = [
    {
        'author': 'Bruno',
        'title': 'blog post 1',
        'content': 'text words',
        'date_posted': 'yesterday'
    },
    {
        'author': 'Bruno',
        'title': 'blog post 2',
        'content': 'text words',
        'date_posted': 'today'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="home", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)



if __name__== '__main__':
    app.run(debug=True)