# dataElectionScenario
An projet which transform data from 2022 and 2024 legislative elections to transform it in json file for an other project

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-red.svg)
![Tests](https://img.shields.io/badge/unit_tests-OK-green.svg)

## Sommaire
- [Installation](#installation)
- [Use](#use)
- [Tests](#tests)
- [Structure du projet](#structure-of-project)
- [Autors](#autors)

## Installation 
Clone the project : 
```bash
git clone https://github.com/plouiserre/dataElectionScenario.git
cd dataElectionScenario
```

Install all dependencies : 
```bash
pip install -r requirements.txt
```

## Use
Execute the program with this command line and replace path_results by the path where the json files will be generate: 
```bash
python main.py "path_results"
```

## Tests
Execute all tests : 
```bash
python -m unittest discover -s tests
```

## Structure of project
```
DataElectionsScenarios
├─── domain/
├─── infrastructure/
│   ├───adapter/   
│   ├───factory/
│   ├───files/
│   ├───memory/
│   ├───services/
├───openDatas/
├───tests
│   ├───utils/
└───usecases/
    ├───AdaptResultElectionData/
    ├───ports/
    │   └───outside/
main.py 
```

## Autors
**Pierre-Louis Serré** – Principle Developer