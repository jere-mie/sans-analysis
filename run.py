from website import app, db
import os
if __name__=='__main__':
    if not os.path.exists("website/site.db"):
        db.create_all()
    if not os.path.exists("website/static/uploads"):
        os.mkdir("website/static/uploads")
    app.run(debug=True)