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

run: ## Run the application cluster
	@echo "$(YELLOW)Running the application cluster...$(RESET)"
	docker compose up --build

run_producer: ## Run the producer service
	@echo "$(YELLOW)Running the producer service...$(RESET)"
	docker compose up --build log_producer