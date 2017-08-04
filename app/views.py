from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is the chefi index!!!"