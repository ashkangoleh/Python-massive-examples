from functools import wraps
from flask import Flask, request


app = Flask(__name__)

def check_auth(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'message': 'No authorization token provided'}, 400
        try:
            user = request.headers['authorization']
            request.user = user
        except:
            return {'message':'Invalid token provided.'}, 400
        return f(*args, **kwargs)
    return wrap

@app.route('/is_subscribed', methods=['POST'])
@check_auth
def is_subscribed():
    if request.method == 'POST':
        try:
            itemId = request.get_json()['item_id']
            print("==>> itemId: ", itemId)
            
            return {
                'message': 'User is subscribed to this item',
                    'status': 'success',
                    'data': True
                }, 200
        except Exception as e:
            return {
                'message': 'Error checking subscription', 
                'status': 'error'
            }, 400


if __name__ == '__main__':
    app.run(debug=True)