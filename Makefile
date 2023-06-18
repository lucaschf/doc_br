SRC_DIRS := doc_br
TEST_DIR := tests
CACHE_DIR := cache

COVERAGE_FAIL_UNDER := 80


.PHONY: install format lint cc tests

## @ dev
install:
	@ rm -rf $(CACHE_DIR)
	# Instalando...
	@ pip install -U pip
	@ poetry install
	# Instalando pre-commit...
	@ pre-commit install
	# Instalando gitlint...
	@ gitlint install-hook

## @ dev
format:  ## Formata o código
	@ isort $(SRC_DIRS) --use-parentheses --line-length=100 --multi-line=3 --trailing-comma
	@ black $(SRC_DIRS) --line-length=100
	@ autoflake --in-place --remove-all-unused-imports -r $(SRC_DIRS)

## @ dev
format-tests:  ## Formata o código de tests
	@ isort $(TEST_DIR) --use-parentheses --line-length=100 --multi-line=3 --trailing-comma
	@ blue $(TEST_DIR) --line-length=100
	@ autoflake --in-place --remove-all-unused-imports -r $(TEST_DIR)

## @ CI
lint: ## Executa a checagem estática (isort, black, flake8 e pydocstyle...).
	# linters
	@ isort --check --diff --use-parentheses --line-length=100 --multi-line=3 --trailing-comma $(SRC_DIRS)
	@ black --check $(SRC_DIRS) --line-length=100
	@ flake8 --max-line-length=100 $(SRC_DIRS)
	@ pydocstyle $(SRC_DIRS)

test: ## Executa os testes
	pytest tests/ -x


.PHONY: help
help:
	@ python -c \
		'import fileinput, re; \
		off, white, darkcyan = "\033[0m", "\033[1;37m", "\033[36m"; \
		lines = (re.search("([a-zA-Z_-]+):.*?## (.*)$$", line) for line in fileinput.input()); \
        methods = filter(None, lines); \
        template = "  "+darkcyan+"  {:10}"+off+" {}"; \
        formatted_methods = sorted(template.format(*method.groups()) for method in methods); \
        print(f"\n  usage: make {darkcyan}<command>\n"); \
        print(f"{white}COMMANDS:"); \
        print("\n".join(formatted_methods))\
        ' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
