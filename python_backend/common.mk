.PHONY: clean
clean:
	@echo "cleaning venv"
	rm -rf venv
.PHONY: create
create:
	@echo "creating venv..."
	PYTHONPATH=. python -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	pip install --upgrade pip

.PHONY: check
check:
	@echo "checking solution..."
	. venv/bin/activate
	python -m unittest -v

.PHONY: all
all:
	@make clean create check
