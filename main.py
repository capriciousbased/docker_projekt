from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6397)

@app.route('/')
def index():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return 'Welcome to the Web App with Python Flask!, This webpage has been viewed {} times.\n'.format(counter)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
