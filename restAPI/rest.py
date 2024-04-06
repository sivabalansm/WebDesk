from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

machine_put_args = reqparse.RequestParser()
machine_put_args.add_argument("name", type=str, help="Name of the machine is required", location="form")
machine_put_args.add_argument("machine_type", type=str, help="Machine type is required", location="form")
with open("machines.json", "r") as f:
    a = f.read()
    if len(a) > 0:
        machines = json.loads(a)
        print(type(machines), machines)
    else:
        machines = dict()


class FlaskConnection(Resource):
    def put(self, machine_id):
        #create
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
        machines.pop(machine_id)
        string = json.dumps(machines)
        open("machines.json", "w").write(string)
        return ""

api.add_resource(FlaskConnection, "/rest/<string:machine_id>")

if __name__ == "__main__":
    app.run(debug=True)
