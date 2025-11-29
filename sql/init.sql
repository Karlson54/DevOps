-- Create notes table
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index on created_at for faster sorting
CREATE INDEX IF NOT EXISTS idx_notes_created_at ON notes(created_at DESC);

-- Insert sample data
INSERT INTO notes (title, content) VALUES
    ('Welcome Note', 'This is your first note in the DevOps Lab 7 application!'),
    ('Docker Tips', 'Remember to use docker-compose up -d to run containers in detached mode.'),
    ('PostgreSQL Info', 'PostgreSQL is running in a separate container with persistent volume.');

-- Create trigger to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_notes_updated_at BEFORE UPDATE ON notes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();