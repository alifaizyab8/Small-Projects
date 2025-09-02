from flask import Flask, render_template, request

app = Flask(__name__)

def convert_number(number, base):
    try:
        #Convert input string to integer
        decimal = int(number, base)
        return{
            'decimal': str(decimal),
            'binary': bin(decimal)[2:], # Remove '0b' prefix
            'octal': oct(decimal)[2:],  # Remove '0o' prefix
            'hexadecimal': hex(decimal)[2:].upper() # Remove '0x' prefix
        
        }
    except ValueError:
        return{'error': 'Invalid number for the specified base.'}
    
@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        number = request.form.get('number')
        base = int(request.form.get('base'))
        results = convert_number(number, base)

    return render_template('index.html', results=results)    
if __name__ == '__main__':
    app.run(debug=True)