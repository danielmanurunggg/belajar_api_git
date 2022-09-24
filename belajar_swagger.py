from flask import Flask, request, jsonify
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
import re

app = Flask(__name__) # deklarasi Flask
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'percobaan SWAGGER'),
        'version': LazyString(lambda: '1'),
        'description': LazyString(lambda: 'ini belajar swagger dengan flask')
    },
    host = LazyString(lambda: request.host)
)

swagger_config = {
    "headers":[],
    "specs": [
        {
            "endpoint":"docs",
            "route":"/docs.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path":"/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger = Swagger(app, template=swagger_template,config=swagger_config)

# def _remove_punct(s):
#     return re.sub(r"[^\w\d\s]+", "", s)

# @app.route("/clean_text/v1", methods=['POST'])
# def remove_punct_post():
#     s = request.get_json()
#     non_punct = _rexmove_punct(s['text'])
#     return jsonify({"hasil_bersih":non_punct})

@swag_from("swagger_config.yml", methods=['GET'])
@app.route("/get_text/v1", methods=['GET']) # ini adalah decorator
def return_text():
    name_input = request.args.get('name')
    print(name_input)
    return_text = {
        "text":f"Halo semuanya! nama saya adalah {name_input}"
    }
    return jsonify(return_text) # supaya bisa return dalam bentuk JSON

if __name__ == "__main__":
    app.run(port=1234, debug=True) # debug ==> kode otomatis update ketika ada perubahan