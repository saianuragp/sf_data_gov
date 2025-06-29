-- NOTE :: Basic Redaction for Emails

CREATE MASKING POLICY mask_email AS (val STRING) 
  RETURNS STRING ->
    CASE 
      WHEN CURRENT_ROLE() IN ('DATA_PRIVILEGED', 'SECURITY_ADMIN') THEN val
      ELSE CONCAT('xxxxx@', SPLIT_PART(val, '@', 2))
    END;

ALTER TABLE patient_data MODIFY COLUMN email SET MASKING POLICY mask_email;


-- NOTE :: Partial Masking for Phone Numbers

CREATE MASKING POLICY mask_phone AS (val STRING)
  RETURNS STRING ->
    CASE 
      WHEN CURRENT_ROLE() IN ('DATA_PRIVILEGED') THEN val
      ELSE CONCAT('(***) ***-', RIGHT(val, 4))
    END;

-- NOTE :: Fully Redacted for SSN

CREATE MASKING POLICY mask_ssn AS (val STRING)
  RETURNS STRING ->
    CASE 
      WHEN CURRENT_ROLE() = 'DATA_PRIVILEGED' THEN val
      ELSE '***-**-****'
    END;
