#!/bin/bash

# Database initialization script for DevOps Lab 7
# Usage: ./init_db.sh [container_name]

set -e

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Default container name
CONTAINER_NAME="${1:-devops_postgres}"

echo -e "${YELLOW}Starting database initialization...${NC}"

# Check if container is running
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo -e "${RED}Error: Container '${CONTAINER_NAME}' is not running!${NC}"
    echo "Please start the containers with: docker-compose up -d"
    exit 1
fi

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo -e "${RED}Error: .env file not found!${NC}"
    exit 1
fi

echo -e "${GREEN}Container found: ${CONTAINER_NAME}${NC}"
echo -e "${GREEN}Database: ${POSTGRES_DB}${NC}"
echo -e "${GREEN}User: ${POSTGRES_USER}${NC}"

# Wait for PostgreSQL to be ready
echo -e "${YELLOW}Waiting for PostgreSQL to be ready...${NC}"
sleep 3

# Execute SQL initialization
echo -e "${YELLOW}Executing SQL initialization script...${NC}"
docker exec -i "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" < sql/init.sql

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Database initialized successfully!${NC}"
    
    # Show tables
    echo -e "${YELLOW}Checking created tables...${NC}"
    docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "\dt"
    
    # Show sample data
    echo -e "${YELLOW}Sample data:${NC}"
    docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "SELECT * FROM notes;"
else
    echo -e "${RED}✗ Database initialization failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Done!${NC}"