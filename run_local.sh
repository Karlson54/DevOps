set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Starting Flask application locally...${NC}"

if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
    export POSTGRES_HOST=localhost
else
    echo -e "${RED}Error: .env file not found!${NC}"
    exit 1
fi

if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

source venv/bin/activate

echo -e "${YELLOW}Installing dependencies...${NC}"
pip install -q -r requirements.txt

echo -e "${GREEN}Starting application on http://localhost:5000${NC}"
echo -e "${GREEN}Press Ctrl+C to stop${NC}"
python app/main.py