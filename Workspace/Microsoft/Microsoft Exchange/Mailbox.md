# Microsoft Exchange

## Mailbox

- Mailboxes are the primary messaging and collaboration tool for users in an Exchange organization.
- Exchange Mailbox is associated with an Active Directory user account.
- Each mailbox consists of an Active Directory user and the mailbox data which is stored in the Exchange mailbox database.

### <u>**Create User Mailbox**</u>

- There are <u>**(2) types**</u> of mailbox creation:
  1. Non-Existing AD User: Automatically create an AD user and enable mailbox to that user
  2. Existing AD User: Directly enable mailbox to the existing user
<br>

- Delete AD User: When an AD user is deleted, the associated Exchange mailbox will also be deleted.
- Disconnect Mailbox: When the mailbox is disconnected from an AD user, only Exchange mailbox data will be deleted.
<br>

<u>Get All User Mailboxes</u>

```powershell
Get-Mailbox
Get-Mailbox -Identity <mailbox_name>
Get-Mailbox -Identity <mailbox_name> | fl Name, DisplayName, Alias, Database
```

<u>Create New Mailbox for Non-Existing AD User</u>

```powershell
New-Mailbox -Name "<Name>" -Alias "<alias>" `
    -UserPrincipalName "<username>@<domain>" `
    -OrganizationalUnit "<domain>/Users" `
    -FirstName "<first_name>" -LastName "<last_name>" `
    -DisplayName "<display_name>" `
    -Password (ConvertTo-SecureString -String 'P@s5w0rd' -AsPlainText -Force) `
    -ResetPasswordOnNextLogon $true
```

<u>Enable Mailbox for Existing AD User</u>

```powershell
Enable-Mailbox -Identity <user>@<domain> -Database <database_name>
```

### <u>**Mailbox Quota**</u>

In Microsoft Exchange, mailbox quotas ensure that users do not exceed storage allocations and help maintain system performance.

#### Types of Mailbox Quotas

1. **Issue Warning Quota:** Users receive a warning email when their mailbox reaches this size.
2. **Prohibit Send Quota:** Users cannot send new emails when this limit is reached.
3. **Prohibit Send/Receive Quota:** Users cannot send or receive emails once this limit is reached.

```powershell
Set-Mailbox <identity> `
    -UseDatabaseQuotaDefaults $false `
    -IssueWarningQuota 1.9GB `
    -ProhibitSendQuota 2GB `
    -ProhibitSendReceiveQuota 2.5GB
```