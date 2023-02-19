import os
from taskmanager import app, db


if __name__ == "__main__":

    def create_tables(self):
        with app.app_context():
            export PGHOSTADDR=127.0.0.1
            db.create_all()
    create_tables(db)
    app.run(
        host=os.environ.get("IP"), 
        port=os.environ.get("PORT"),
        debug=os.environ.get("DEBUG")
    )

    

    
