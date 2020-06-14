from flask import render_template, jsonify
from app import app
from app.models import Image

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/image/<int:id>',methods=['Get'])
def get_image(id):
    return jsonify(Image.query.get_or_404(id).to_dict())
