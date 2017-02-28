imlsof:
	PYTHONPATH=~/experiments/gcc_py_introspector/ python3 ./manage.py import --settings=introspector.settings.development ../lsof

mkmig:
	python3 ./manage.py makemigrations --settings=introspector.settings.development  gcc_tu_parser

sqlmigrate:
	python3 ./manage.py sqlmigrate --settings=introspector.settings.development gcc_tu_parser 0001_initial
migrate:
	python3 ./manage.py migrate --settings=introspector.settings.development gcc_tu_parser

# 0001_initial
# 0002_auto_20170222_1008
# 0003_auto_20170222_1009

test:
	PYTHONPATH=~/experiments/gcc_py_introspector/ python3 ./manage.py runserver --settings=introspector.settings.development

collect:
	python3 ./manage.py bower install --settings=introspector.settings.development 
	python3 ./manage.py  collectstatic --settings=introspector.settings.development

analyze:
	python3 ./manage.py analyse --settings=introspector.settings.development color function_type prms tree_list function_params

analyze2:
	python3 ./manage.py analyse --settings=introspector.settings.development color enumeral_type	csts	tree_list enum_consts



dbshell:
	python3 ./manage.py dbshell --settings=introspector.settings.development 
