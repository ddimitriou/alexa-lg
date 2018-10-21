## Alexa LG TV control

This stand alone service's purpose is to run in a server like environment in your local network and provide a set of controls for your LG Smart TV operated via your Amazon Echo.

For now we are exposing:


1. on/off
2. channel up/down
3. netflix on/off


After you follow the Configuration and the service is running, all you have to do is call alexa:


1. `alexa Television on` to turn it on -- off respectively
2. `alexa Netflix on` for opening `Netflix` app.
3. `alexa Channel on` to change the channel up (or off to change the channel down).


But its up to you to create more functionality.

This library works by incorporating two different projects into one.
It uses: [Fauxmo](https://github.com/n8henrie/fauxmo) and [LGWebOSRemote](https://github.com/klattimer/LGWebOSRemote)
all at the latest version.

For now using `fauxmo` we can create different devices where only the functions on/off are supported.

You need at least python3.6 for this to run.

## Configuration

Install [virtualenv](https://virtualenv.pypa.io/en/stable/), for unix OS
For Windows, follow [these](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/) instructions

Then, run:


```
make env
source env/bin/activate
make system_deps
```

For initial setup, you must do:

```
./env/bin/python3 Alexa/AlexaLG.py setup
```

Wait for the prompt from your LG, and accept it via the remote control.

Then to keep running:

```
make run
```

Tested to work with the latest Web-OS v3.0 LGTV
