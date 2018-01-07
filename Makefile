# Unit-testing, docs, etc.

VIRTUALENV?=venv
ENV?=env
TEST?=nosetests


env: rm -fr $(ENV)
	$(VIRTUALENV) --no-site-packages $(ENV)
	system_deps
	@echo "\n\n>> Run 'source $(ENV)/bin/activate'"

system_deps:
	pip install -r requirements.txt

run: clean
	@echo "\nStarting Fauxmo server\n"
	PYTHONPATH=`pwd` $(ENV)/bin/python3 src/alexa_lg.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	@echo "done"

test: clean
	PYTHONPATH=`pwd` APPLICATION_ENV=test $(ENV)/bin/nosetests --rednose --with-notify tests
