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

### 3. Run Auto-Tagging

```python
python auto_tag_phi_columns.py
```




Certainly! Below is the **complete, ready-to-paste `README.md`** file for your GitHub repo focused on automating PHI/PII governance in Snowflake using Python and SQL.

You can copy this directly into your repository.

---

````markdown
# 🧊 Snowflake PHI/PII Data Governance Toolkit

A plug-and-play toolkit for automating **PHI/PII protection** in Snowflake using dynamic masking, tagging, and policy enforcement — designed to work seamlessly with **Medallion Architecture (Bronze → Silver → Gold)**.

> ⚠️ Perfect for healthcare, insurance, fintech, and any regulated data workloads in Snowflake.

---

## 📦 What's Included

| File/Folder | Description |
|-------------|-------------|
| `auto_tag_phi_columns.py` | Python script to scan columns for PHI/PII patterns and apply tags |
| `masking_policy_templates.sql` | Snowflake masking policy examples (email, SSN, phone, etc.) |
| `row_access_policy_templates.sql` | Row-level access policies based on geography or role |
| `data_governance_playbook.md` | A compliance checklist across Bronze, Silver, and Gold layers |
| `examples/` | Sample outputs and usage walkthroughs |

---

## ✅ Features

- Automatic tagging of PHI/PII fields using regex pattern matching
- Plug-and-play masking policies (fully/partially masked by role)
- Row access filtering for geo-restriction or role-based segmentation
- Secure by design for Medallion Lakehouse patterns
- Built with HIPAA, GDPR, SOC 2 alignment in mind

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/snowflake-phi-governance.git
cd snowflake-phi-governance
````

### 2. Configure Snowflake Credentials

Edit the `auto_tag_phi_columns.py` file with your Snowflake credentials:

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

## 📋 Governance Playbook Overview

| Layer      | Focus                              | Controls                   |
| ---------- | ---------------------------------- | -------------------------- |
| **Bronze** | Raw ingestion of PHI/PII           | Tagging, limited access    |
| **Silver** | Cleaned, structured sensitive data | Masking, RLS, RBAC         |
| **Gold**   | Analytics-ready, governed output   | Views only, access history |

Full checklist in: `data_governance_playbook.md`

---

## 📌 Example Use Case

🏥 A healthcare company unintentionally exposed PHI from Silver to a Gold dashboard. After applying this toolkit:

* All PII/PHI fields were tagged + masked dynamically
* Analysts only saw masked data via secure views
* Role hierarchy + access logging were enforced

⏱️ Time to remediate: <48 hours

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
📫 Contact: [LinkedIn Profile](https://linkedin.com/in/your-profile)
🔗 Article: ["Safeguarding PHI/PII in Snowflake Medallion Architecture"](https://www.linkedin.com/in/your-profile/posts/)

> Drop a ⭐ if this helps your team, and open an issue if you'd like to contribute templates for dbt, Airflow, or Snowpark!

---

```

---

### ✅ Next Steps:
- Replace placeholders like `your-org`, `your-profile`, and repo links.
- Optionally add badges (Python version, license, etc.) if publishing publicly.

Would you like a matching `data_governance_playbook.md` file next?
```
