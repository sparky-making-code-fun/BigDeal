#This is just a template to use for building stuff.
#It will need to be majorly redone
target ?= dev
branch ?= develop


dev1 = 54.86.86.181

qa1 = 54.84.192.143

prod1 = 54.84.87.69
prod2 = 54.84.86.37

deps:
	pip install -r setup/requirements/$(target).txt
	pip install -r setup/requirements/common-gannett.txt

test: deps
	python manage.py test --noinput

unittest: deps
	python manage.py test --failfast --noinput --exclude=integrationtests/*.py

deploy: $(target)

dev:
	ssh -t -t -o StrictHostKeyChecking=no nowu@$(dev1) "cd boomers-web; make target=dev update"

qa:
	ssh -t -t -o StrictHostKeyChecking=no nowu@$(qa1) "cd boomers-web; make target=qa branch=$(branch) update"

prod:
	ssh -t nowu@$(prod1) "cd boomers-web; make target=prod branch=master update_primary"
	ssh -t nowu@$(prod2) "cd boomers-web; make target=prod branch=master update_secondary"

setup_env:
	. /etc/profile.d/nowu.sh

git_pull:
	git stash
	git fetch
	git checkout $(branch)
	git pull origin $(branch)

get_reqs:
	pip install -r setup/requirements/$(target).txt
	pip install -r setup/requirements/common-gannett.txt

syncdb:
	python manage.py syncdb --noinput
	python manage.py migrate --noinput

collectstatic:
	npm install && bower install && grunt bowercopy
	python manage.py collectstatic --noinput

restart_web:
	sudo service uwsgi restart
	sudo service nginx restart

restart_workers:
	sudo service celeryd restart
	sudo service celerybeat start
	sudo service celerycam start

coverage:
	coverage run --source='.' --omit=*settings*,*wsgi*,*djangoratings*,*googleanalytics*,*tests*,*migrations*,*site-packages* manage.py test
	coverage html


update_primary: setup_env git_pull get_reqs syncdb collectstatic restart_web restart_workers

update_secondary: setup_env git_pull get_reqs restart_web

update: update_primary
