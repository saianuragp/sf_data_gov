import snowflake.connector
import re

# Define regex patterns for PII/PHI fields
PII_PATTERNS = {
    'email': r'email',
    'ssn': r'ssn',
    'dob': r'dob|date[_]?of[_]?birth',
    'phone': r'phone|mobile',
    'address': r'address',
    'name': r'first[_]?name|last[_]?name|full[_]?name'
}

# Snowflake credentials
conn = snowflake.connector.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

cursor = conn.cursor()

def apply_tag_to_column(table_name, column_name, tag_name='PHI_TAG', tag_value='YES'):
    try:
        sql = f"""
        ALTER TABLE {table_name}
        MODIFY COLUMN {column_name}
        SET TAG {tag_name} = '{tag_value}';
        """
        cursor.execute(sql)
        print(f"[TAGGED] {table_name}.{column_name}")
    except Exception as e:
        print(f"[ERROR] {table_name}.{column_name}: {str(e)}")

def scan_and_tag():
    cursor.execute("""
        SELECT table_name, column_name
        FROM information_schema.columns
        WHERE table_schema = CURRENT_SCHEMA();
    """)
    columns = cursor.fetchall()

    for table, column in columns:
        for label, pattern in PII_PATTERNS.items():
            if re.search(pattern, column, re.IGNORECASE):
                apply_tag_to_column(table, column)
                break  # Skip to next column after first match

scan_and_tag()
cursor.close()
conn.close()
