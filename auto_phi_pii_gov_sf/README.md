# 🧊 Snowflake PHI/PII Data Governance Toolkit

This repository contains automation scripts, masking policy templates, and governance playbooks to help teams safeguard **Protected Health Information (PHI)** and **Personally Identifiable Information (PII)** in **Snowflake's Medallion Architecture**.

---

## 📦 What’s Included

| File | Description |
|------|-------------|
| `auto_tag_phi_columns.py` | Python script to auto-detect and tag PHI/PII columns based on regex |
| `masking_policy_templates.sql` | SQL templates for common masking policies (SSN, Email, Phone, etc.) |
| `row_access_policy_templates.sql` | Templates for region- or role-based access filtering |
| `data_governance_playbook.md` | Checklist for PHI/PII handling across Bronze, Silver, Gold layers |
| `examples/` | Example outputs, policy applications, and sample schema |

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
