from flask import Flask
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app=Flask(__name__)
app.config.from_object('config')
path_image=app.config['PATH_IMAGE']
manager=Manager(app)
db=SQLAlchemy(app)
migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(
        use_debugger = True,
        use_reloader = True))

from life import views, models
