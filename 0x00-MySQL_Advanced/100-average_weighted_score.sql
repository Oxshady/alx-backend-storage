-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

DELIMITER $$
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN A_user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    SELECT SUM(c.score * p.weight) INTO total_score,
        SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = A_user_id;

    IF total_weight > 0 THEN
        UPDATE users SET average_score = total_score / total_weight WHERE id = A_user_id;
    ELSE
        UPDATE users SET average_score = 0 WHERE id = A_user_id;
    END IF;
END$$
DELIMITER ;
