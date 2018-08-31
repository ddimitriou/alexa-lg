# Unit-testing, docs, etc.

VIRTUALENV?=virtualenv
ENV?=env
TEST?=nosetests


env:
	rm -fr $(ENV)
	$(VIRTUALENV) --no-site-packages -p python3 $(ENV)
	@echo "\n\n>> Run 'source $(ENV)/bin/activate'"

system_deps:
	pip3 install -r requirements.txt

run: clean
	@echo "\nStarting Fauxmo server\n"
	PYTHONPATH=`pwd` $(ENV)/bin/python3 Alexa/AlexaLG.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	@echo "done"

test: clean
	PYTHONPATH=`pwd` APPLICATION_ENV=test $(ENV)/bin/nosetests --rednose --with-notify tests

.PHONY: