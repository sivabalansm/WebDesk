#! /bin/python3
from flask import Flask, jsonify, request
from flask_cors import CORS
import manager

app = Flask(__name__)
CORS(app)


@app.route('/machines')
def get_machines():
    machines = [{container.name: [container.status, 6080 + int(container.name[2:])]} for container in manager.ls_cont_name()]
    print(machines)
    return jsonify(machines)


@app.route('/create', methods=['POST', 'OPTIONS'])
def create_instance():
    resp = request.get_json()
    print(resp)
    if resp['type'] == 'win':
        inst = manager.create('win_inst2')
        print(inst.name)
        machine = {inst.name: [inst.status, 6080 + int(inst.name[2:])]}
        response = jsonify(machine)
        response.headers.add('Access-Control-Allow-Origin', '*')

        print(machine)
        return response
    return '',200

@app.route('/restart', methods=['POST'])
def restart_instance():
    resp = request.get_json()
    for machine in manager.ls_cont_name():
        if resp['id'] == machine.name:
            manager.restart(machine.name)
            return '', 204

    return '', 204

@app.route('/stop', methods=['POST'])
def stop_instance():
    resp = request.get_json()
    for machine in manager.ls_cont_name():
        if resp['id'] == machine.name:
            manager.stop(machine.name)
            return '', 204
    return '', 204
    

@app.route('/delete', methods=['POST'])
def delete_instance():
    resp = request.get_json()
    for machine in manager.ls_cont_name():
        if resp['id'] == machine.name:
            manager.delete(machine.name)
            return '', 204
    return '', 204


