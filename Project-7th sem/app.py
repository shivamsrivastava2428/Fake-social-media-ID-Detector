from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def is_fake_social_media_id(username):
    """
    Simple heuristic to determine if a social media ID might be fake.
    For demo purposes, here are some example rules:
    - Too short or too long usernames are considered fake
    - Usernames with suspicious patterns like lots of digits only are fake
    - Usernames with special characters are fake
    - Otherwise, considered real
    """
    if not username:
        return True
    username = username.strip()
    if len(username) < 3 or len(username) > 30:
        return True
    if username.isdigit():
        return True
    if any(char in username for char in " !@#$%^&*()+=[]{}|\\;:'\"<>,.?/~`"):
        return True
    # Here, you could add more complex pattern checks or API checks.
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    username = data['username']
    if is_fake_social_media_id(username):
        result = 'Fake'
    else:
        result = 'Real'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
