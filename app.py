from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from img import process_image
from spellcheck import llama_spell_correction

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', image_urls=[], extracted_texts=[], current_index=0)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'images' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('images')
    image_urls = []
    extracted_texts = []

    for image in files:
        if image.filename == '':
            continue

        if image:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            extracted_text = process_image(image_path)
            image_url = url_for('static', filename='uploads/' + image.filename)
            image_urls.append(image_url)
            extracted_texts.append(extracted_text)

    return render_template(
        'index.html',
        image_urls=image_urls,
        extracted_texts=extracted_texts,
        current_index=0
    )

@app.route('/spell_check', methods=['POST'])
def spell_check():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    try:
        corrected_text = llama_spell_correction(text)
        return jsonify({
            'success': True,
            'corrected_text': corrected_text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
