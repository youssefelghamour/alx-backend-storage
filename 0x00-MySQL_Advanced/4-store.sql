-- SQL script that creates a trigger that automatically updates the quantity of items in the 'items' table by
-- subtracting the ordered amount ('number') whenever a new order (for the item) is inserted into the 'orders' table.
DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$
DELIMITER ;
