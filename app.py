from flask import Flask, render_template, jsonify, send_from_directory # type: ignore
import os
import random
from prompts import prompts

app = Flask(__name__)

# 이미지 경로 설정
IMAGE_FOLDER = '/Users/kangminjung/woosung/Writing/static/images'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_prompt', methods=['GET'])
def get_prompt():
    prompt = random.choice(prompts)
    return jsonify(prompt=prompt)

@app.route('/get_image', methods=['GET'])
def get_image():
    image_files = [f for f in os.listdir(app.config['IMAGE_FOLDER']) if f.endswith(('png', 'jpg', 'jpeg'))]
    image = random.choice(image_files)
    return jsonify(image=image)

@app.route('/static/images/<filename>')
def images(filename):
    return send_from_directory(app.config['IMAGE_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
