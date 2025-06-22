from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

@app.route('/geogebra-link', methods=['POST'])
def geogebra_link():
    data = request.get_json()
    equation = data.get('equation', '')
    url_equation = urllib.parse.quote(equation)
    geogebra_url = f"https://www.geogebra.org/graphing?query={url_equation}"
    return jsonify({
        "geogebra_link": geogebra_url
    })

if __name__ == '__main__':
    app.run(port=5000)