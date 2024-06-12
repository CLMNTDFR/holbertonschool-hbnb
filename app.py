from flask import Flask
from Persistence.DataManager import DataManager
from api.user_routes import user_bp  # Importez le blueprint user_bp

app = Flask(__name__)
db = DataManager()

# Enregistrez le blueprint user_bp
app.register_blueprint(user_bp, url_prefix='/users')

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
