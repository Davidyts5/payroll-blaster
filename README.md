# Payroll Blaster

Simple Python SMTP email blaster script for Android (Termux) and PC.

## How to Use

1. Edit the SMTP config in `payroll_blaster.py`:
   ```python
   smtp_server = "smtp.gmail.com"   # or mail.hostinger.com etc.
   smtp_port = 465
   sender_email = "your-email@domain.com"
   sender_pass = "your-password-or-app-pass"
2. Create or edit leads.txt with this exact format:
Manager Name|manager.email@company.com|Worker Name|Position
Example:
Louis Greco|lgreco@orthony.com|Lindsay Sparano|Medical Assistant
Run the script:
python payroll_blaster.py

Made for testing and educational purposes.
