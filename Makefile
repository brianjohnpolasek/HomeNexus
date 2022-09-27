FLASK_APP = app.py
FLASK := FLASK_APP=$(FLASK_APP) env/bin/flask

.PHONY: setup
setup:
	test -d env || python3 -m env
	. env/bin/activate && pip3 install --default-timeout=100 -r requirements.txt

.PHONY: run
run:
	FLASK_DEBUG=1 $(FLASK) run

.PHONY: run-prod
run-prod:
	FLASK_DEBUG=0 $(FLASK) run

.PHONY: clean
clean:
	deactivate
	rm - rf env
	find -iname "*.pyc" - delete
