from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello PetFax!"
    
    # Register the app
    from . import pet
    from . import facts
    app.register_blueprint(pet.bp)
    app.register_blueprint(facts.bp)

    # Return app
    return app