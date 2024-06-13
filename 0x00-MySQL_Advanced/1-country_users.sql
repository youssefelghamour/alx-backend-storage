-- SQL script that creates a new table users
-- country VARCHAR(2) NOT NULL DEFAULT 'US' CHECK (country in ('US', 'CO', 'TN'))
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
