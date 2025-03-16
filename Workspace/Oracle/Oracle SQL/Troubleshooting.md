# Oracle SQL

## Troubleshooting

### <u>ORA-01034: Oracle Not Available</u>

##### Check if Database is Running

```console
sqlplus / as sysdba
```

If it says: **Connected to an idle instance**, the database is not started.

##### Start Database

```sql
STARTUP;
```

[![xl](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/oracle/oracle-sql/troubleshooting/oracle-sql-troubleshooting-001.PNG)](https://s3.us-east-1.amazonaws.com/stephenphyo.github.io/oracle/oracle-sql/troubleshooting/oracle-sql-troubleshooting-001.PNG)