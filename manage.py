from flask import Flask,render_template
from config import create_app,db
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate


app = create_app()
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()