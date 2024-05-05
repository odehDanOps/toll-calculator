from app.main import create_app
from config import DevelopmentConfig

config = DevelopmentConfig
app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')