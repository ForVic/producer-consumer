from flask import Flask
import time 
import random
from flask_cors import CORS
from celery import Celery
"""
Note that for this to work using the current implementation you must be running a version of 
Python3, Python3.9 or lower.:wq
"""

app = Flask(__name__)
cors = CORS(app)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def background_task():
  for i in range(10):
    with open(f"file_{i}", "w") as f:
      f.write("test")
    time.sleep(random.randint(1, 10) * .1)

@app.route("/", methods=["GET"])
def start():
  background_task.apply_async(countdown=5)
  return "Starting", 200

if __name__ == "__main__":
  app.run(debug=True)
