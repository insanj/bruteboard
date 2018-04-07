PYTHON=py -2

all: clean setup run clean

run:
	$(PYTHON) run.py

setup:
	conda install -y pip
	pip install pypiwin32
	conda install -y psutil

clean:
	del /S *.pyc