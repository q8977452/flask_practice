from flask import Flask, make_response, request,Response
import time

app = Flask(__name__)

@app.route("/set")
def setcookie():
    resp = make_response('Setting cookie!')
    resp.set_cookie(key='framework', value='flask', expires=time.time()+6*60)
    return resp

@app.route("/get")
def getcookie():
    framework = request.cookies.get('framework')
    return 'The framework is ' + framework

@app.route('/del')
def del_cookie():
    res = Response('delete cookies')
    res.set_cookie(key='framework', value='', expires=0)
    return res

if __name__ == '__main__':
    app.run(debug=True)