-- SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed
DELIMITER $$
CREATE TRIGGER reset_validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = NOT OLD.valid_email;
    END IF;
END $$
DELIMITER ;
