
setup:
	pip3 install --user -r requirements.txt

test: setup
	nosetests --with-coverage --cover-html test_gilded_rose.py

results: test
	firefox cover/index.html

create-master:
	python3 texttest_fixture.py 20 > master.txt

check-master:
	python3 texttest_fixture.py 20 | diff master.txt -
