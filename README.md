# Payroll Blaster

Simple Python SMTP script for sending batch emails from Android (Termux) or PC.

## Features
- Random subjects and message bodies
- Visible random delay between emails (60-140 seconds)
- Works with Gmail, Hostinger, or any SMTP provider
- Easy leads.txt format

## Step-by-Step Setup

 1.  Clone the Repository
```bash
git clone https://github.com/Davidyts5/payroll-blaster.git
cd payroll-blaster
 2. Configure SMTP
Edit the config:
nano payroll_blaster.py
Update these lines:
smtp_server = "smtp.gmail.com"        # Change to your provider 
smtp_port = 465
sender_email = "your-email@domain.com"      # Your email
sender_pass = "your-password-or-app-pass"   # Your password or App Password
Save: Ctrl + X → Y → Enter
3. Prepare leads.txt
nano leads.txt
Use this format (one per line):
Manager Name|manager.email@company.com|Worker Name|Position
Example:
Louis Greco|lgreco@orthony.com|Lindsay Sparano|Medical Assistant
Save: Ctrl + X → Y → Enter
4. Run the Script
python payroll_blaster.py

Notes
Start with small batches (10-20 leads)
The script shows success/failure and wait time for each email
Edit sender_email and sender_pass with your own credentials before running
Made for learning and testing purposes.
