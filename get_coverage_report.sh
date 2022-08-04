coverage run --source modules.api.src -m unittest discover && coverage report
coverage run --source modules.database.src -m unittest discover && coverage report
coverage run --source modules.utils.src -m unittest discover && coverage report