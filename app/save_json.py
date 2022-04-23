import json

from app.constants import FILES


def save_json_file(machine_list):
    machines = {}
    for machine in machine_list:
        machines[machine[0]] = {
            "cpu / vcpu": machine[1],
            "memory": machine[2],
            "storage / ssd disk": machine[3],
            "bandwitch / transfer": machine[4],
            "price [$/mo]": machine[5],
        }

    with open(FILES["json"], "w") as jsonFile:
        jsonFile.write(json.dumps(obj=machines, indent=4, ensure_ascii=False))
