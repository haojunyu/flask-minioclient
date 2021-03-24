deploy:
	python3 -m pip install pipenv
	export PIPENV_VENV_IN_PROJECT=1 && pipenv intall -d
build:
	pipenv run python setup.py sdist bdist_wheel
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf Flask_MinioClient.egg-info
publish:
	pipenv run twine upload dist/*