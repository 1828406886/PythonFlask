from flask import Flask, url_for ,request
app = Flask(__name__)
@app.route('/')
def index():
	return 'index'

@app.route('/hello')
def hello_world():
	return 'Hello world!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
def show_the_login_for():
	return 'login'


if __name__=='__main__':
	app.debug = True
	app.run()
