## Requirements
Python >= 3.8

MongoDB (using 5.0.9)

## Install
* Installing virtual environment
```sh
python3 -m venv bot-env
```

* Installing required packages/libraries
```sh
pip install -r requirements.txt
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
./bot-env/Scripts/activate
```

* Run the python script
```sh
python3 bot.py
```
