# 0x00. MySQL advanced

## Overview

This project focuses on advanced MySQL concepts and practices. It includes SQL scripts that demonstrate various skills such as table creation, data manipulation, stored procedures, triggers, and indexing.

## Files

| File Name             | Description                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------|
| 0-uniq_users.sql      | Creates a users table with unique email constraint and specified attributes.                    |
| 1-country_users.sql   | Creates a users table with an additional country column and enumerated values.                   |
| 2-fans.sql            | Ranks country origins of bands based on fan count.                                               |
| 3-glam_rock.sql       | Lists bands specializing in Glam rock, ranked by longevity.                                       |
| 4-store.sql           | Implements a trigger to decrease item quantity upon adding new orders.                            |
| 5-valid_email.sql     | Implements a trigger to reset valid_email attribute when the email is changed.                   |
| 6-bonus.sql           | Defines a stored procedure AddBonus to add corrections for students.                              |
| 7-average_score.sql   | Defines a stored procedure ComputeAverageScoreForUser to compute and store average scores for students. |
| 8-index_my_names.sql  | Creates an index idx_name_first on the first letter of name in the names table.                   |
| 9-index_name_score.sql         | Creates an index idx_name_first_score on names table for first letter of name and score.               |
| 10-div.sql                     | Defines function SafeDiv to safely divide two numbers, returning 0 if second number is 0.               |
| 11-need_meeting.sql            | Defines view need_meeting listing students with score < 80 and no recent meeting date.                  |
| 100-average_weighted_score.sql | Defines procedure ComputeAverageWeightedScoreForUser to calculate weighted score for a user.           |
| 101-average_weighted_score.sql | Defines procedure ComputeAverageWeightedScoreForUsers to calculate weighted score for all users.      |
