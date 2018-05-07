from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e784ae3c10c94269f19f9bdcaee5f34a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Corey Schaffer',
        'title': 'Repository 1',
        'content': 'Project using python',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Akim Benchiha',
        'title': 'Repository 2',
        'content': 'Project using python and flask',
        'date_posted': 'May 20, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About Akim\'World')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register in Akim\'s World', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@akim.com' and form.password.data == 'password':
            flash('You have been logged in ! ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check tour credentials', 'danger')
    return render_template('Login.html', title='Login in Akim\'s World', form=form)

if __name__ == '__main__':
    app.run(debug=True)