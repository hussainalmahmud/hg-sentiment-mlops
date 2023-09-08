install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=greeting \
		~-covesmath --coveweb tests	
	python -m pytest --nbval notebook.ipynb #tests our jupyter notebook 
	#python -m pytest -v tests/test_web.py #if you just want to test web
debug:
	python -m pytest -v --pdb #Debugger is invoked
one-test:
	python -m pytest -v tests/test_greeting.py::test_my_name4




# test:
# 	python -m pytest -vv --cov=hello test_hello.py
# format:
# 	black *.py

# lint:
# 	pylint --disable=R,C hello.py

# all: install lint test format 