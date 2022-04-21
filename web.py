import os, string, random
from flask import *

webApp = Flask(__name__, template_folder = "index")

def main():
    #Configure flask and it's settings such as upload path and allowed extensions
    webApp.run(host="0.0.0.0", debug = True, port=int(os.environ.get("PORT", 8080)))

    #Redirect user to index.html
    web()


@webApp.route("/")
def web():
    with webApp.app_context():
        return render_template("index.html")

if __name__ == "__main__":
    main()
