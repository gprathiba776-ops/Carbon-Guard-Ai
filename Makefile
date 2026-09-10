.PHONY: test

test:
	python -m py_compile backend/calculator-api/app.py backend/factor-api/app.py
