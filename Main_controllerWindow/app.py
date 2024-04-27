from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/url',methods=['GET','POST'])
def robot_parameters():
    if request.method =='GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found', 404

if __name__ == '__main__':
   app.run(debug=True)