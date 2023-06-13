from flask import Flask, render_template, request, jsonify
# from cloudant.client import Cloudant
from ibmcloudant import CouchDbSessionAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)
# client = Cloudant(, url="")
# client = Cloudant.iam("YmAyXYha4ESFcGI--eim6XBuET1xE412UhYQcA81FT7L", "https://64d6c53a-6850-49f7-8aef-0dbac919dc28-bluemix.cloudantnosqldb.appdomain.cloud")
# authenticator = CouchDbSessionAuthenticator("64d6c53a-6850-49f7-8aef-0dbac919dc28-bluemix", "YmAyXYha4ESFcGI--eim6XBuET1xE412UhYQcA81FT7L")
# authenticator = IAMAuthenticator('YmAyXYha4ESFcGI--eim6XBuET1xE412UhYQcA81FT7L')
# cloudant = CloudantV1(authenticator=authenticator)
# cloudant.set_service_url("https://64d6c53a-6850-49f7-8aef-0dbac919dc28-bluemix.cloudantnosqldb.appdomain.cloud")



# Homepage
@app.route('/')
def home():
    return render_template('base.html')

# Calendar page
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

# Flask routes
@app.route('/api/events', methods=['GET'])
def get_events():
    # Connect to the Cloudant database
    # cloudant.   .connect()
    response = cloudant.post_find(
        db='vacations',
        # doc_id='your_document_id'
        selector={}
    ).get_result()
    # cloudant.disconnect()
    print(response)
    event_data = response['docs']
    return jsonify(event_data), 200

@app.route('/api/events', methods=['POST'])
def add_event():
    event = request.json
    
    # Connect to the Cloudant database
    # cloudant.connect()
    response = cloudant.post_document(
        db='vacations',
        document=event
    ).get_result()
    # cloudant.disconnect()
    
    return jsonify(response), 201

@app.route('/api/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    # Connect to the Cloudant database
    # cloudant.connect()
    response = cloudant.delete_document(
        db='vacations',
        doc_id=event_id
    ).get_result()
    # cloudant.disconnect()
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
