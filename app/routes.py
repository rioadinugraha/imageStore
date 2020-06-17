from app import app
from flask import jsonify,request,url_for
from app.models import Image
from app.errors import bad_request
from app import db

# @app.route('/images/<int:id>',methods=['Get'])
# def get_image(id):
#     return jsonify(Image.query.get_or_404(id).to_dict())

@app.route('/images/<string:filename>',methods=['Get'])
def get_image(filename):
    data = Image.query.filter_by(image_filename=filename).first_or_404()
    return jsonify(data.to_dict())

@app.route('/images/',methods=['Post'])
def post_image():
    data = request.get_json() or {}
    if 'image_url' not in data or 'image_filename' not in data:
        return bad_request('image json needs to be in data ')
    image = Image()
    image.from_dict(data)
    db.session.add(image)
    db.session.commit()
    response = jsonify(image.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_image', filename=image.image_filename)
    return response
