from flask import Flask, request, jsonify

import picDetect

# This is a server to connect Flutter with python using flask
app = Flask(__name__)


@app.route('/singleDetection', methods=['GET'])
def returnPerc():
    d = {}
    url = str(request.args['img'])
    perc = picDetect.detection(url)
    d['percentage'] = perc
    print(d)
    return d


if __name__ == '__main__':
    app.run(debug=True)
