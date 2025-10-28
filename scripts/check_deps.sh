#!/bin/bash
# Check and install dependencies automatically

check_python() {
    if ! command -v python3 &> /dev/null; then
        echo "Error: Python 3 is not installed"
        echo "Please install Python 3: https://www.python.org/downloads/"
        exit 1
    fi
}

check_pip() {
    if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
        echo "Error: pip is not installed"
        echo "Please install pip: https://pip.pypa.io/en/stable/installation/"
        exit 1
    fi
}

install_pyyaml() {
    if python3 -c "import yaml" 2>/dev/null; then
        return 0
    fi
    
    echo "Installing PyYAML..."
    if command -v pip3 &> /dev/null; then
        pip3 install --user pyyaml -q
    else
        pip install --user pyyaml -q
    fi
    
    if [ $? -eq 0 ]; then
        echo "✓ PyYAML installed"
        return 0
    else
        echo "Error: Failed to install PyYAML"
        echo "Please run: pip install pyyaml"
        exit 1
    fi
}

check_python
check_pip
install_pyyaml
