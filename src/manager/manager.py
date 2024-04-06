#! /bin/python3

import docker

client = docker.from_env()

def prep():
    pass

def getLatestID():
    big_num = -1
    for container in client.containers.list(all=True):
        containerName = container.name
        if "WD" == containerName[:2] and containerName[2:].isdigit() and int(containerName[2:]) > big_num:
            big_num = int(containerName[2:])

    return big_num + 1


def create(machine_type):
    latestID = getLatestID()
    return client.containers.run(machine_type, ports = { '6080/tcp' : 6080 + latestID }, detach = True, devices = ['/dev/kvm'], name = f'WD{latestID}')


def restart(name):
    for container in client.containers.list(all=True, filters = {'status': 'exited'}):
        if container.name == name:
            container.start()
            return container


def stop(name):
    for container in client.containers.list(all=True, filters = {'status': 'running'}):
        containerName = container.name
        if containerName == name:
            container.stop()
            return container




def delete(name):
    for container in client.containers.list(all=True):
        if container.name == name and container.status == 'running':
            container.stop()
            break

    for container in client.containers.list(all=True):
        if container.name == name and container.status == 'exited':
            container.remove()

def ls_cont_name():
    return [container for container in client.containers.list(all=True) if container.name[:2] == 'WD']        

if __name__ == "__main__":
    #create('ub_inst2')
    #create('win_inst2')
    #stop('WD1')
    #print(restart('WD1'))

    delete('WD0')
    print(ls_cont_name())

