from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e784ae3c10c94269f19f9bdcaee5f34a'

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