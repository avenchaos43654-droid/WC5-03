from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json() or {}
    original_text = data.get('user_input', '')
    
    result = ""
    shift_factor = 0
    
    if original_text.strip():
        x = original_text.upper()
        words = x.split()
        shift_factor = len(words[0]) if words else 0 
        
        p = ""
        for i in x:
            if i.isalpha():
                k = ALPHABETS.index(i)
                o = ALPHABETS[(k - shift_factor) % 26]    
                p += f"{o}"
            else:
                p += i
        result = p
    else:
        result = ""
        shift_factor = 0

    return jsonify({
        "result": result,
        "shift_factor": shift_factor
    })

if __name__ == '__main__':
    app.run(debug=True)