import os

# sets the base directory to the directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(
        basedir, "instance", "app.db"
    )


if __name__ == "__main__":
    print("sqlite:///" + os.path.join(basedir, "instance", "app.db"))
    print(basedir)
