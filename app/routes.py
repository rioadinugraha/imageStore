from app import app
from flask import jsonify,request,url_for
from app.models import Image
from app.errors import bad_request
from app import db

@app.route('/image/<int:id>',methods=['Get'])
def get_image(id):
    return jsonify(Image.query.get_or_404(id).to_dict())


@app.route('/image/',methods=['Post'])
def post_image():
    data = request.get_json() or {}
    if 'image' not in data:
        return bad_request('image json needs to be in data ')
    image = Image()
    image.from_dict(data, new_user=True)
    db.session.add(image)
    db.session.commit()
    response = jsonify(image.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=image.id)
    return response
