from flask import Flask,jsonify


app = Flask(__name__)
Telephone_book=[{'id_no':"1",
                 'name':"ishan",
                 'tel_no':"076234234"},
                {'id_no': "2",
                 'name': "kisal",
                 'tel_no': "076234233"}
                ]

@app.route('/')

def index():
    return "Welcome to ishan API"


@app.route("/Telephone_book",methods=['GET' ])
def get():
    return jsonify({'Telephone_book':Telephone_book})

@app.route("/Telephone_book/<int:id>",methods=['GET' ])
def get_name(id):
    return jsonify({'Telephone_book': Telephone_book[id-1]})



if __name__ =="__main__":
    app.run(debug=True)

# Print dictionary

