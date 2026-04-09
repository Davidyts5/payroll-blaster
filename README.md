# Payroll Blaster🚀

Simple Python SMTP script for sending batch emails.

Works on **Android (Termux)** and **PC (Windows/Mac/Linux)**.

## Features⚒️
- Random subjects and message bodies
- Visible random delay between emails (60-140 seconds)
- Works with Gmail, Hostinger, or any SMTP provider
- Easy `leads.txt` format

## Step-by-Step Setup (Same for Termux and PC)

### 1. Clone the Repository
```bash
git clone https://github.com/Davidyts5/payroll-blaster.git
cd payroll-blaster
```
### 2. Configure SMTP
Edit the config file:
On Termux:
```bash
nano payroll_blaster.py
```
On PC: Open 
```bash
payroll_blaster.py
```
with any text editor (Notepad, VS Code, etc.)
Update these lines:
```bash
smtp_server = "smtp.gmail.com"        # Change if using other provider
smtp_port = 465
sender_email = "your-email@domain.com"      # ← Your full email
sender_pass = "your-password-or-app-pass"   # ← Your password or App Password
```
Save the file.

### 3. Prepare leads.txt
Create or edit leads.txt:
On Termux: 
```bash
nano leads.txt
```
On PC: Open with any text editor
Use this exact format (one lead per line):
```bash
Manager Name|manager.email@company.com|Worker Name|Position
```
Example:
```bash
Louis Greco|lgreco@orthony.com|Lindsay Sparano|Medical Assistant
```
Save the file.

### 4. Run the Script
On Termux: 
```bash
python payroll_blaster.py
```
On PC: 
```bash
python payroll_blaster.py
```
OR 
```bash
python3 payroll_blaster.py
```
on Mac/Linux if the first one doesn't work

Notes

-Start with small batches (10-20 leads) to avoid spam flags.

-The script shows success/failure and wait time for each email.

-Always edit sender_email and sender_pass with your own credentials before running.


## Made for learning and testing purposes.
