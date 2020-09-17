# Serverless Mathematical Functions

## GCP Cloud Function Deployment

```
POST https://us-central1-quick-dimension-289822.cloudfunctions.net/klarna-functions-dev-math
```

Execution examples:
```
Body
{
    "function": "fibonacci",
    "data": {
        "n": 6
    }
}

Response
{
    "result": 8
}

---------

Body
{
    "function": "fibonacci_naive",
    "data": {
        "n": 6
    }
}

Response
{
    "result": 8
}

---------

Body
{
    "function": "factorial",
    "data": {
        "n": 6
    }
}

Response
{
    "result": 720
}

---------

Body
{
    "function": "ackermann",
    "data": {
        "m": 3,
        "n": 4 
    }
}

Response
{
    "result": 125
}

---------

Body
{
    "function": "ackermann_naive",
    "data": {
        "m": 3,
        "n": 4 
    }
}

Response
{
    "result": 125
}
```

## How to deploy:
\<project\> is a placeholder for the target GCP project name.

You need to copy the GCP project service account key to ~/.gcloud and name it \<project\>.json

Then, run the following commands to deploy it to GCP:
```
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
npm install
serverless deploy --stage dev --project <project>
```

## Running locally
Run the following commands to run a local Flask Application for testing purposes:
```
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then, you can
```
POST http://127.0.0.1:5000/
```

With the same results as the GCP deployment

## Running tests:
```
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
pytest
```

## Running test coverage report:
```
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
pytest --cov
```