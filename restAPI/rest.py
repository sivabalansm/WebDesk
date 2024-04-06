from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
#app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///database.db'
#db = SQLAlchemy()
"""
class MachineModel(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    machine_type = db.Column(db.String(100), nullable=False)

    def __repr(self):
        return f"Machine(name = {name}, machine_type = {machine_type}"
"""
#db.create_all()     #temp command, run only once

machine_put_args = reqparse.RequestParser()
machine_put_args.add_argument("name", type=str, help="Name of the machine is required", location="form")
machine_put_args.add_argument("machine_type", type=str, help="Machine type is required", location="form")
file = open("machines.json", "r").read()
print(file)
machines = json.loads(file) if file else {}

class FlaskConnection(Resource):
    def put(self, machine_id):
        #create
        ip = machine_id
        args = machine_put_args.parse_args()
        machines[machine_id] = args
        json.dump(machines, open("machines.json", "w"))
        return machines[machine_id]

    def get(self, machine_id):
        #run
        return machines[machine_id] 

    def patch(self, machine_id):
        #stop
        return machines[machine_id]

    def delete(self, machine_id):
        del machines[machine_id]
        json.dump(machines, open("machines.json", "w"))
        return ""

api.add_resource(FlaskConnection, "/rest/<int:machine_id>")

if __name__ == "__main__":
    app.run(debug=True)
