set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

CONTAINER_NAME="${1:-devops_postgres}"

echo -e "${BLUE}=== Database Verification ===${NC}\n"

if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo -e "${RED}Error: .env file not found!${NC}"
    exit 1
fi

if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo -e "${RED}Error: Container '${CONTAINER_NAME}' is not running!${NC}"
    exit 1
fi

echo -e "${YELLOW}Container: ${CONTAINER_NAME}${NC}"
echo -e "${YELLOW}Database: ${POSTGRES_DB}${NC}"
echo -e "${YELLOW}User: ${POSTGRES_USER}${NC}\n"

echo -e "${GREEN}📋 Tables in database:${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "\dt"
echo ""

echo -e "${GREEN}📊 Structure of 'notes' table:${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "\d notes"
echo ""

echo -e "${GREEN}📈 Number of records:${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "SELECT COUNT(*) as total_notes FROM notes;"
echo ""

echo -e "${GREEN}📝 Sample data (first 5 records):${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "SELECT id, title, LEFT(content, 50) as content_preview, created_at FROM notes LIMIT 5;"
echo ""

echo -e "${GREEN}🔍 Indexes:${NC}"
docker exec "${CONTAINER_NAME}" psql -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'notes';"
echo ""

echo -e "${GREEN}✓ Database verification completed!${NC}"