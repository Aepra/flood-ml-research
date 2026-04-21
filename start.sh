#!/bin/bash
# ============================================================
#   Flood ML Research - One Command Setup
#   Simply run: ./start.sh
# ============================================================

echo ""
echo "============================================================"
echo "         FLOOD ML RESEARCH - Starting Docker"
echo "============================================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker not found!"
    echo ""
    echo "Please install Docker Desktop from:"
    echo "  https://www.docker.com/products/docker-desktop"
    echo ""
    exit 1
fi

# Start Docker Compose
echo "Starting container... (this may take a few minutes on first run)"
echo ""

docker-compose up

echo ""
echo "============================================================"
echo "         Container stopped"
echo "============================================================"
echo ""
