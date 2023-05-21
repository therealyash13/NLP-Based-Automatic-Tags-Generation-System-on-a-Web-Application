
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer

import gzip
import pickle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

fp = gzip.open('./import/model_all.pkl', 'rb')
model_all = pickle.load(fp)

model = model_all[0]
termFrequencyVectorizer = model_all[1]
multilabelBinarizer = model_all[2]

@app.route('/')
def hello_world():
    return '<h1>Hello, Welcome to Repurpost Web API!</h1>'


# GET requests will be blocked
@app.route('/suggestTags', methods=['POST'])
@cross_origin()
def suggest_Tags():
    request_data = request.get_json()

    contentText = request_data['content']
    content = []
    content.append(contentText.lower())

    print(content)

    prediction = model.predict(termFrequencyVectorizer.transform(content))
    tags = list(multilabelBinarizer.inverse_transform(prediction))

    return tags
