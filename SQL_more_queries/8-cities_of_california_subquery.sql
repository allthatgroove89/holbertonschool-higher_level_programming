-- Script that creates database hbtn_0d_usa and table states
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
