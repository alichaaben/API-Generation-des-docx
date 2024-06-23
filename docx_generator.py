from docxtpl import DocxTemplate
from app import app
from flask import jsonify, Response
from flask import flash, request
import json
import os
from docx2pdf import convert
from flask import Flask
app = Flask(__name__)

def generate_doc(source, output, file, data):
    doc = DocxTemplate(source)
    context = data
    doc.render(context)
    os.makedirs(output, exist_ok=True)
    doc.save(output+"/"+file)
    #convert(output+"/"+file, "outpout_tamplate.pdf")



@app.route('/generate', methods=['POST'])
def generate_doc_service():
    body = request.json
    source = body["source_path"]
    data = body["data"]
    output = body["output_path"]
    file_name = body["output_file_name"]

    generate_doc(source, output, file_name, data)

    return body


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)



# doc = DocxTemplate("my_word_template.docx")
# context = { 'company_name' : "World company" }
# doc.render(context)
# doc.save("generated_doc.docx")