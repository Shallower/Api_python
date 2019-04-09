from flask_script import Manager, Server
from main import app, db, User, Video

manager = Manager(app)
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Video=Video)


if __name__ == "__main__":
    manager.run()
