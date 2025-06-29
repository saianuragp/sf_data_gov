-- NOTE :: Role-Based Policy for Multiple Use Cases

CREATE MASKING POLICY mask_based_on_role AS (val STRING)
  RETURNS STRING ->
    CASE 
      WHEN CURRENT_ROLE() IN ('DATA_PRIVILEGED', 'PII_REVIEWER') THEN val
      ELSE NULL
    END;


