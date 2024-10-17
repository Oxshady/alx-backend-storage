-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET user_id = NULL;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO user_id;

        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

        SELECT SUM(c.score * p.weight) INTO total_score,
            SUM(p.weight) INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        IF total_weight > 0 THEN
            UPDATE users SET average_score = total_score / total_weight WHERE id = user_id;
        ELSE
            UPDATE users SET average_score = 0 WHERE id = user_id;
        END IF;
    END LOOP;

    CLOSE user_cursor;
END$$
DELIMITER ;
