from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def count_telor(text):
  text = re.sub(r"[^\w\d\s]+", "", text).lower()
  text = text.split()
  sum = text.count('telor')
  return sum

def count_len(text) : return len(text)

def check_name(name):
    if name.lower() == "jokowi":
        return_text = {
            "nama":"ya ndak tau kok tanya saya"
        }
    else:
        return_text = {
            "nama":f"nama beliau adalah {name}"
        }
    return return_text

@app.route("/get_name/v1", methods=['GET'])
def return_text():
    name_input = request.args.get('nama')
    return_name = check_name(name_input)
    return jsonify(return_name)

@app.route("/post_text/v1", methods=['POST'])
def return_count():
    s = request.get_json()
    a = count_len(s['text'])
    b = count_telor(s['text'])
    return_text = {
        "total_char":a,
        "total_telor":b
    }
    return jsonify(return_text)

if __name__ == '__main__':
    app.run(port=1234, debug=True)