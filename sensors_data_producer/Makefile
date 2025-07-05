# Define colors
GREEN := \033[0;32m
YELLOW := \033[0;33m
RESET := \033[0m

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "$(YELLOW)Available targets:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-30s$(RESET) %s\n", $$1, $$2}'

format:
	poetry run black . --line-length 120

lint:
	poetry run flake8 . --config=pyproject.toml