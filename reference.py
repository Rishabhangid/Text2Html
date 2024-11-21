from flask import Flask, request, jsonify
import app

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    markdown_text = data.get('markdown')
    
    # Convert markdown to HTML
    html = app.app(markdown_text)
    
    return jsonify({'html': html})

if __name__ == '__main__':
    app.run(debug=True)
