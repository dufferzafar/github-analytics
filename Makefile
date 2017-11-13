default: clean

clean:
	@rm -rf metastore_db
	@rm -rf src/metastore_db
	@rm -f derby.log
	@rm -f src/derby.log

pip-dump:
	env/bin/pip freeze > requirements.txt

zip:
	@git archive --format=zip master > team-0-github-analytics.zip
