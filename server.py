from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    try:
        locations = util.get_location_names()
        response = jsonify({'locations': locations})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 500

@app.route('/', methods=['POST'])
def predict_home_price():
    try:
        print(request.form)  # Log the incoming form data

        total_sqft = float(request.form["total_sqft"])
        location = request.form['location']
        BHK = int(request.form['BHK'])
        bath = int(request.form['bath'])

        estimated_price = util.estimated_price(location, total_sqft, BHK, bath)

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 500

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)
