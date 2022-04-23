import csv

from app.constants import FILES

header = ["machine", "cpu / vcpu", "memory", "storage / ssd disk", "bandwitch / transfer", "price [$/mo]"]


def save_csv_file(machine_list):
    with open(FILES["csv"], "w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(header)

        for machine in machine_list:
            writer.writerow(machine)
