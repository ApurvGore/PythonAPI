from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'Missing "text" in the request body'}), 400

        english_text = data['text']
        french_translation = translator.translate(english_text, src='en', dest='fr').text

        response_data = {'translation': french_translation}
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
