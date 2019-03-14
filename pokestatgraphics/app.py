from flask import Flask, render_template, request
from .models import df

def create_app():
    ''' create and configure an instance of the Flask application '''
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['ENV'] = 'debug' # TODO: Change beffore deploying
    
    #DB.init_app(app)
    
    @app.route("/")
    def root():
        #users = User.query.all()
        print(df)
        return render_template('base.html', title='Home', dat=df.values)

    return app
