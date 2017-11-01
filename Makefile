default: clean

clean:
	@rm -rf metastore_db
	@rm -rf src/metastore_db
	@rm -f derby.log
	@rm -f src/derby.log

pip-dump:
	env/bin/pip freeze > requirements.txt
