## Requirements
Python >= 3.8

MongoDB (using 5.0.9)

* Install & activate virtual environment
```sh
virtualenv venv --python=python38
source venv/bin/activate
```

* Installing required packages/libraries
```sh
poetry install
```

* Installing dependencies
```sh
sudo apt install libffi-dev libnacl-dev python3-dev
```

* Create .env and update required fields
```sh
cp env.example .env
```

## Running the project

* Activate virtual environment
```sh
source venv/bin/activate
```

* Run the python script
```sh
python3 main.py
```
