import requests
from parsel import Selector

from app.constants import PAGE_TARGET
from app.helpers import (
    set_new_prices_list,
    set_new_units_list,
    set_new_values_list_target_1,
    set_new_values_list_target_2,
)


def crawler(number_page_target):
    url = PAGE_TARGET[number_page_target]
    text = requests.get(url).text
    selector = Selector(text=text)

    if number_page_target == 1:
        machine_list = page_target_1_process(selector)
    else:
        machine_list = page_target_2_process(selector)

    return machine_list


def page_target_1_process(selector):
    divs_all_machines = selector.xpath('//div[@class="row row--eq-height packages"]')
    machines_list = divs_all_machines.xpath('//div[@class="col-lg-3"]')

    machine_list = []
    index_values_list = [0, 1, 2, 3, 4]
    index_units_list = [1, 3, 4]

    for index, machine in enumerate(machines_list):
        key = (machine.xpath('//h3[@class="package__title h6"]/text()')[index].get()).strip()
        values_list = machine.xpath('//li[@class="package__list-item"]//b/text()').getall()
        units = [
            unit.replace("\n", "").replace("\t", "")
            for unit in machine.xpath('//li[@class="package__list-item"]/text()').getall()
        ]

        if index < len(machines_list) - 1:
            machine = [
                key,
                (
                    f"{values_list[index_values_list[1]]}{units[index_units_list[1]]} "
                    f"{values_list[index_values_list[2]]}{units[index_units_list[2]]}"
                ),
                values_list[index_values_list[3]],
                f"{values_list[index_values_list[0]]}{units[index_units_list[0]]}",
                values_list[index_values_list[4]],
                machine.xpath('//span[@class="price__value"]/b/text()')[index].get(),
            ]
            machine_list.append(machine)
        else: # the last machine has two specifications about SSD/Disk, so it needs extra implementations
            machine = [
                key,
                f"{values_list[20]}{units[29]} {values_list[21]}{units[30]}",
                values_list[index_values_list[4]],
                (
                    f"{values_list[index_values_list[0]]}{units[index_units_list[0]]}"
                    f" / {values_list[index_values_list[1]]}{units[index_units_list[1]]}"
                ),
                values_list[23],
                machine.xpath('//span[@class="price__value"]/b/text()')[index].get(),
            ]
            machine_list.append(machine)

        index_values_list = set_new_values_list_target_1(index_values_list)
        index_units_list = set_new_units_list(index_units_list)

    return machine_list


def page_target_2_process(selector):
    section_all_machines = selector.xpath('//section[@id="pricing-card-container"]')
    machines_list = section_all_machines.xpath('//div[re:test(@class, "pricing-card ")]')

    machine_list = []
    index_values_list = [0, 2, 4, 6]
    index_prices_list = [0, 1]

    for index, machine in enumerate(machines_list):
        values_list = machine.xpath('//li[@class="pricing-card-list-items"]/text()').getall()
        prices_list = machine.xpath('//p[@class="pricing-card-price"]/text()').getall()
        machine = [
            machine.xpath('//h3[@class="pricing-card-title"]/text()')[index].get(),
            values_list[index_values_list[1]],
            values_list[index_values_list[0]],
            values_list[index_values_list[2]],
            values_list[index_values_list[3]],
            f"{prices_list[index_prices_list[0]]} {prices_list[index_prices_list[1]]}",
        ]
        machine_list.append(machine)

        index_values_list = set_new_values_list_target_2(index_values_list)
        index_prices_list = set_new_prices_list(index_prices_list)

    return machine_list
