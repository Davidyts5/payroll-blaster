import smtplib
from email.mime.text import MIMEText
import time
import random
import datetime

print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Payroll Blaster - Initial Blast Only")

# === SMTP CONFIG - CHANGE THESE ===
# Works with Gmail, Hostinger, Outlook, etc.
smtp_server = "smtp.gmail.com"        # Change if using other provider
smtp_port = 465                       # Usually 465 for SSL, 587 for TLS
sender_email = "your-email@domain.com"      # ← Put your full email address here
sender_pass = "your-password-or-app-pass"   # ← Put your password or App Password here

# Subjects
subjects = [
    "Quick Update: My Direct Deposit Info",
    "Payroll Deposit Change Needed",
    "New Bank Details for Upcoming Payroll",
    "Request to Update My Banking Information",
    "Urgent: Direct Deposit Update",
    "My Bank Account Changed - Please Update",
    "Payroll Banking Update Request"
]

# 10 natural body variants
bodies = [
    """Hi {manager},

My bank is having some issues with my current direct deposit. Can you please send me the form to update my banking details for the next payroll?

Thanks,
{worker}
{position}""",

    """Hi {manager},

I need to update my direct deposit information. Could you send me the payroll change form?

Appreciate it,
{worker}
{position}""",

    """Hi {manager},

Quick question - my bank account changed recently. Please send the direct deposit update form so I can get it sorted before payday.

Thanks,
{worker}
{position}""",

    """Hi {manager},

I'm switching banks and need to update my payroll deposit. Can you please send me the direct deposit change form?

Best,
{worker}
{position}""",

    """Hi {manager},

My current bank setup is causing problems with payroll. Please send the form so I can update my account details.

Thank you,
{worker}
{position}""",

    """Hi {manager},

I just opened a new account and would like to change where my paycheck goes. Can you send me the update form?

Thanks,
{worker}
{position}""",

    """Hi {manager},

There’s an issue with my direct deposit. Could you please forward the payroll banking change form?

Appreciate your help,
{worker}
{position}""",

    """Hi {manager},

I need to make a change to my direct deposit for the next pay period. Please send me the required form.

Regards,
{worker}
{position}""",

    """Hi {manager},

My bank recently updated their system and I need to verify my payroll deposit details. Can you send the change form?

Thank you,
{worker}
{position}""",

    """Hi {manager},

Please send me the direct deposit update form. I need to change my banking information before the next payroll cycle.

Best regards,
{worker}
{position}"""
]

# Load leads
with open("leads.txt", "r", encoding="utf-8") as f:
    leads = [line.strip() for line in f.readlines() if line.strip() and "|" in line]

print(f"Loaded {len(leads)} leads. Starting initial blast...\n")

success_count = 0
fail_count = 0

for i, line in enumerate(leads, 1):
    try:
        parts = line.split("|")
        manager_name = parts[0].strip()
        manager_email = parts[1].strip()
        worker_name = parts[2].strip()
        position = parts[3].strip()

        subject = random.choice(subjects)
        body = random.choice(bodies).format(manager=manager_name, worker=worker_name, position=position)

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = f"{worker_name} <{sender_email}>"
        msg["To"] = manager_email

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_pass)
        server.sendmail(sender_email, manager_email, msg.as_string())
        server.quit()

        print(f"[{i}/{len(leads)}] ✅ SUCCESS - Sent to {manager_email} as {worker_name} ({position})")
        success_count += 1

    except Exception as e:
        print(f"[{i}/{len(leads)}] ❌ FAILED - {manager_email} | {str(e)[:80]}")
        fail_count += 1

    # Visible random wait time
    wait_time = random.randint(60, 140)
    print(f"   ⏳ Waiting {wait_time} seconds before next email...")
    time.sleep(wait_time)

print("\n" + "="*70)
print("INITIAL BLAST COMPLETE")
print("="*70)
print(f"Total Leads          : {len(leads)}")
print(f"Successfully Sent    : {success_count} ✅")
print(f"Failed               : {fail_count}")
print("="*70)
print("Now wait for HR replies with the form, then send your real bank details.")
