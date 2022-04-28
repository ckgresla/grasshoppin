/* Question Link- https://leetcode.com/problems/patients-with-a-condition/ */


SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'
					  -- 1st condition finds all occurences of DIAB1 that occur after the first token in the "conditions" string
					  -- 2nd Condition finds all the instances where the first item in the string is a DIAB1 (starts w this medical condition)


