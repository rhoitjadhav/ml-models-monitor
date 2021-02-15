# ML-Models-Monitoring System

ML Models Monitoring system allows you to monitor the models which are being used in production. It monitors performance metrics of the models.

## Installation

install.sh will install all dependencies required to run this application which includes python 3, pip, sqlite database and other required packages which is defined in requirements.txt. Additionally it will ask you for the permission to install the pacakges.

```bash
./install.sh
```

## Requirements

Python 3 and pip will be installed via install.sh file which is covered in Installation section. In ubuntu 18.04 python 3 is built-in package which is already installed in the system.

- Ubuntu 18.04
- Python 3.6
- pip
- Sqlite3 Database

## Run application

Before running application we need to train and push monitoring data to database of ML Models which are defined in `ml_models` folder. We are using two machine learning models i.e `housing_price` & `payment_fraud`. The following script will train and push monitoring data to database.

Note: `pipenv shell` command activates the virtual environment.

```bash
cd ml_models
pipenv shell
python run_model.py
```

There are two servers i.e `ml_monitor` and `ml_models`. In order to run these servers execute the following commands.

### For ML-Monitor

```bash
pipenv shell
cd ml_monitor
python app.py
```

### For ML-Models

```bash
pipenv shell
cd ml_models
python app.py
```

## Run Tests

To run the tests execute the following commands. This will run the tests which are defined in `ml_models/tests` module. 

```bash
pipenv shell
cd ml_models
python test.py
```

## Project Code Structure Overview

Project consists of two main applications i.e ml_monitor and ml_models. Each application is based on flask and its directory structure & file conventions. Same overview is presented below:

- **Pipfile** -> Pipenv configuration file
- **Pipfile.lock** -> Contains packages dependencies configuration
- **app.py** -> Entry point of the application
- **src** -> Application specific modules
- **models** -> Database interface api is defined in this module
- **routes** -> APIs are defined in this module for the applications
- **usecases** -> All the use cases implemented by the application are defined in this module

- **config.py** -> All the application configuration variables are placed in this file
- **db.json** -> Database file
- **run_model.py** -> This program trains the ml models (housing_price, payment_fraud) and push the result to the database
- **test.py** -> By executing this file, it initiates the testing and shows results of test cases
- **housing_price & payment_fraud** -> Machine Learning models
