import argparse

from app.crawler import crawler
from app.print import show
from app.save_csv import save_csv_file
from app.save_json import save_json_file

description = """Get the informations from the websites and show the screen, save in JSON file or save in CSV file.

Run with: $ python app.py --optional-arguments
"""

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
parser.add_argument("--page_target", type=int, help="Run the crawler in page target", choices=range(1, 3))
parser.add_argument("--print", help="Show results on the screen", action="store_true")
parser.add_argument("--save_csv", help="Save data in CSV file", action="store_true")
parser.add_argument("--save_json", help="Save data in JSON file", action="store_true")

args = parser.parse_args()
page_target = args.page_target
show_screen = args.print
save_csv = args.save_csv
save_json = args.save_json

if page_target:
    machine_list = crawler(page_target)

if show_screen:
    show(machine_list)

if save_csv:
    save_csv_file(machine_list)
    print("CSV file stored in data_files/file.csv")

if save_json:
    save_json_file(machine_list)
    print("JSON file stored in data_files/file.json")
