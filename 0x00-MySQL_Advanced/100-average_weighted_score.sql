-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weights INT DEFAULT 0;
    DECLARE weighted_sum FLOAT DEFAULT 0;

    -- Calculate the sum of the weights for the projects the user is involved in
    SELECT SUM(projects.weight)
    INTO total_weights
    FROM projects
    JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;
    
    -- Calculate the sum of (project scores * weights)
    SELECT SUM(corrections.score * projects.weight)
    INTO weighted_sum
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Update the user's average score with the weighted average
    UPDATE users
    SET average_score = IF(total_weights = 0, 0, weighted_sum / total_weights)
    WHERE id = user_id;
END $$
DELIMITER ;
