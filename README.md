# Pooling API Endpoint

## Download the code 
Move to the directory that you want to locate your repository; for example: ~/Documents
```
cd ~/Documents
```
Running following command to pull the repository
```
git clone https://github.com/trungtx92/pool_api.git
```

## Create a virtual environment
Move to respository:
```
cd ~/Documents/pool_api
```

Create the virtual environment from the repository
```
python3 -m venv .venv
```

## Activate the virtual environment
```
source .venv/bin/activate
```

## Install Dependences
```
pip3 install -r requirements.txt
```

## Run the fastAPI Server
```
fastapi dev pools.py
```