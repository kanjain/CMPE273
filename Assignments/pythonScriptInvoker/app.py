#app.py
import sys
import io
import contextlib
import rocksdb
import uuid

from flask import Flask, request, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    db = rocksdb.DB("test.db", rocksdb.Options(create_if_missing=True))
    db.put(b'a', b'Hey, we have Flask in a Docker container!')
    x = db.get(b'a')
    return x


@app.route('/api/<version>/scripts/<script_id>')
def scripts(version, script_id):
    db = rocksdb.DB("test.db", rocksdb.Options(create_if_missing=True))
    scriptToRun = db.get(script_id.encode())

    with stdoutIO() as s:
        exec(scriptToRun)

    return s.getvalue()

@app.route('/api/<version>/scripts', methods=['POST'])
def scripts_post(version):
    db = rocksdb.DB("test.db", rocksdb.Options(create_if_missing=True))
    key = uuid.uuid1().int>>64
    strKey = str(key)
    responseJson = get_script_id(strKey)
    scriptCode = (request.files['data']).read()

    db.put(strKey.encode(), scriptCode)

    return app.response_class(
        response=responseJson,
        status=201,
        mimetype='application/json'
    )

def get_script_id(id):
    result = {'script-id': id}
    return json.dumps(result)

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)