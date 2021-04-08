from website import app
import os
if __name__=='__main__':
    if not os.path.exists("website/static/uploads"):
        os.mkdir("website/static/uploads")
    app.run(debug=True)