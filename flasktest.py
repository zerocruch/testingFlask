from flask import Flask
import threading


#webserver
def webServer():
  app = Flask(__name__)

  @app.route('/', methods=['GET', 'POST'])
  def index():
    return "200OK"

  app.run(host='0.0.0.0', port=80)


web = threading.Thread(target=webServer)  #<<<----- Disable them in production 
web.start() #<<<----------------------------------- Server
