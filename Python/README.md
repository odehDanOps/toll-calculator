# Steps to run on local machine
## Change directory to python
```
cd python
```
## Create and activate virtual env
```
python3 -m venv venv
source venv/bin/activate
```
## Install packages
```
pip install -r requirements.txt"
```
## Run migration
```
flask db init
flask db migrate -m "Initial city database migration"
flask db upgrade
```
## Run database seed
```
flask seed run
```

## Run the application
```
python run.py
```