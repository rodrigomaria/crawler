# Crawler

This project allows the execution of a crawler on the sites described in the file [constants](./app/constants.py).

Has been created using [Python 3.10.4](https://www.python.org/downloads/release/python-3104/) and [Docker](https://docs.docker.com/get-docker/). Please install both technologies.

## Instructions:
1. To build this image, use this Makefile command
```bash
$ make build
```

2. To run container, use this Makefile command
```bash
$ make run
```

3. To run linters about the code, use this Makefile command, if you implement any updates/fixes
```bash
$ make lint
```

## How to use:
1. After generate and run container, use this Makefile command
```bash
$ make sh
```

2. The terminal shell will open. In this shell, the following commands will be invoked:
```bash
$ python app.py --page_target {1,2} --optional-arguments
```

| Argument      | Mandatory       | Values to select | Describe                       |
| ------------- | --------------- | --------------   | ------------------------------ |
| --page_target | Yes             | 1, 2             | Run the crawler in page target | 
| --print       |                 |                  | Show results on the screen     |
| --save_csv    |                 |                  | Save data in CSV file          |
| --save_json   |                 |                  | Save data in JSON file         |

For only show on the screen the informations crawled from page target 1
```bash
$ python app.py --page_target 1 --print
```

For show on the screen and save in json file the informations crawled from page target 1
```bash
$ python app.py --page_target 1 --print --save_json
```

For only save in csv file the informations crawled from page target 1
```bash
$ python app.py --page_target 1 --save_csv
```

Created by: [Rodrigo Maria Morgão](mailto:rodrigo@rodrigomaria.com.br).