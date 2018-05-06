from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)