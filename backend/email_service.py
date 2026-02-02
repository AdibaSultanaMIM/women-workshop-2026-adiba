import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_confirmation_email(to_email, name):
    """Send confirmation email to registered participant"""
    
    # Skip if credentials not configured
    if not os.getenv('GMAIL_USER') or not os.getenv('GMAIL_APP_PASSWORD'):
        print("Email credentials not configured - skipping email")
        return True
    
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = f"WE-ICT 2026 <{os.getenv('GMAIL_USER')}>"
        msg['To'] = to_email
        msg['Subject'] = '✅ Registration Confirmed - WE-ICT 2026'
        
        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #D946A6 0%, #9333EA 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                .content {{ background: #f8f9fa; padding: 30px; border-radius: 0 0 10px 10px; }}
                .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎉 Registration Confirmed!</h1>
                </div>
                <div class="content">
                    <p>Dear <strong>{name}</strong>,</p>
                    <p>Thank you for registering for <strong>WE-ICT 2026: Women Empowerment through ICT</strong>!</p>
                    
                    <h3>Event Details:</h3>
                    <ul>
                        <li>📅 <strong>Date:</strong> February 24, 2026</li>
                        <li>📍 <strong>Location:</strong> Graduate Complex, BUET, Dhaka</li>
                        <li>⏰ <strong>Registration:</strong> 8:30 AM</li>
                        <li>🎯 <strong>Topics:</strong> Higher Studies, Research & Career</li>
                    </ul>
                    
                    <p>We look forward to seeing you at the workshop!</p>
                    
                    <div class="footer">
                        <p>WE-ICT 2026 Organizing Committee<br>
                        Department of CSE, BUET</p>
                        <p style="font-size: 0.8em; color: #999;">For queries, contact: tanzimahashem@gmail.com</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(html_body, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(os.getenv('GMAIL_USER'), os.getenv('GMAIL_APP_PASSWORD'))
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Email error: {e}")
        raise

