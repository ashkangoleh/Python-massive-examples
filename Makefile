install:
	pip install --upgrade pip

format:
	black *.py */*.py

lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py */*.py

test:
	#test
deploy:
	#test

all: install lint test deploy