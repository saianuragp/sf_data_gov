# 🧊 Snowflake PHI/PII Data Governance Toolkit

This repository contains automation scripts, masking policy templates, and governance playbooks to help teams safeguard **Protected Health Information (PHI)** and **Personally Identifiable Information (PII)** in **Snowflake's Medallion Architecture**.

---

## 📦 What’s Included

| File | Description |
|------|-------------|
| `auto_tag_phi_columns.py` | Python script to auto-detect and tag PHI/PII columns based on regex |
| `masking_policy_templates.sql` | SQL templates for common masking policies (SSN, Email, Phone, etc.) |
| `row_access_policy_templates.sql` | Templates for region- or role-based access filtering |
---

## 🧰 Features

- ✅ **Auto-tagging engine** using Snowflake column metadata
- ✅ Easy-to-apply masking policies with role-based redaction
- ✅ Ready-to-use templates for row-level security
- ✅ Designed for **Medallion Architecture** (Bronze → Silver → Gold)
- ✅ Compliant with HIPAA, GDPR, and SOC 2 governance best practices

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/saianuragp/sf_data_gov.git
cd sf_data_gov/auto_phi_pii_gov_sf
```

### 2. Set Up Snowflake Credentials

Update the ```auto_tag_phi_columns.py``` script with your Snowflake account details:

```python
conn = snowflake.connector.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)
```

### 3. Run Auto-Tagging Script

This script identifies columns like `email`, `ssn`, `dob`, etc., and applies a tag (`PHI_TAG` = 'YES').

```bash
python auto_tag_phi_columns.py
```

> 📝 You can customize the regex dictionary in the script to match your organization’s naming standards.

---

## 🔐 Apply Masking Policies

Example: Email masking policy (partial redaction based on role):

```sql
CREATE MASKING POLICY mask_email AS (val STRING)
  RETURNS STRING ->
    CASE
      WHEN CURRENT_ROLE() IN ('DATA_PRIVILEGED') THEN val
      ELSE CONCAT('xxxxx@', SPLIT_PART(val, '@', 2))
    END;

ALTER TABLE patient_data
MODIFY COLUMN email
SET MASKING POLICY mask_email;
```

Other masking policies provided include:

* `mask_ssn`
* `mask_phone`
* `mask_dob`
* `mask_based_on_role`

---

## 🧪 Row Access Policy Template

```sql
CREATE ROW ACCESS POLICY region_filter
  AS (region STRING) RETURNS BOOLEAN ->
    CURRENT_REGION() = region;

ALTER TABLE patient_data
ADD ROW ACCESS POLICY region_filter ON (region);
```

> You can also scope access by `user`, `department`, or `classification`.

---

## 🤝 Contributing

We welcome contributions! To suggest a new masking policy or enhance the auto-tagging logic:

1. Fork this repo
2. Create a feature branch (`feat/new-mask-policy`)
3. Submit a pull request

---

## 🛡 License

MIT License — Free to use, adapt, and extend.
**Do not use this to bypass privacy or compliance standards.**

---

## 📣 Connect & Contribute

Built and maintained by \[Your Name / Org]
📫 Contact: [LinkedIn Profile](www.linkedin.com/in/saianuragp22)

> Drop a ⭐ if this helps your team, and open an issue if you'd like to contribute templates for dbt, Airflow, or Snowpark!

---
