from flask import Flask, render_template, request, make_response
import redis
import os
import json
import uuid

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))


def get_redis():
    return redis.Redis(host=redis_host, port=redis_port)


@app.route('/', methods=['GET', 'POST'])
def vote():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = str(uuid.uuid4())

    vote = None
    if request.method == 'POST':
        vote = request.form.get('vote')
        if vote:
            data = json.dumps({'voter_id': voter_id, 'vote': vote})
            get_redis().rpush('votes', data)

    resp = make_response(render_template('index.html', vote=vote))
    resp.set_cookie('voter_id', voter_id)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
