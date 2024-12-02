from app import createApp
from app.routes import routes

app = createApp()
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
