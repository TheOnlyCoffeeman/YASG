# Define paths and executable name
SRC = src/main.py
WORK_DIR = ./temp
SPEC_DIR = ./specs
EXE_NAME = YASG
VENV_DIR = ./venv

# Default target (build)
all: build

# Clean up old builds
.PHONY: clean
clean:
	rm -rf ./build ./temp game_log.txt $(SPEC_DIR) $(VENV_DIR)

# Create a virtual environment and install requirements
.PHONY: venv
venv: clean
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Build executable
.PHONY: build
build: venv
	@echo "Building..."
	mkdir -p ./build
	$(VENV_DIR)/bin/pyinstaller --onefile --windowed --distpath ./build --workpath $(WORK_DIR) --specpath $(SPEC_DIR) --name $(EXE_NAME) $(SRC)
