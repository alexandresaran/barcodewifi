from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
#Le a informacao atraves de um GET
@app.route('/barcode', methods=['GET', 'POST'])
def barcode():
	content = request.get_json()
	print(content)
	return 'JSON Enviado'

#Ip setado como local 
app.run(host='0.0.0.0')