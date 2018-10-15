## Alexa LG TV control

This stand alone service's purpose is to run in a server like environment in your local network and provide a set of controls for your LG Smart TV operated via your Amazon Echo.

You need at least python3.6 for this to run.

## Configuration

Install virtualenv

```
make env
source $(ENV)/bin/activate
make system_deps
```

For initial setup, you must do:
```
$(ENV)/bin/python3 Alexa/AlexaLG.py setup
```
Wait for the prompt from your LG.

Then to keep running:
```
make run
```
