
setup:
	pip3 install --user -r requirements.txt

test: setup
	nosetests --with-coverage --cover-html test_gilded_rose.py

results: test
	firefox cover/index.html