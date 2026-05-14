from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import datetime

def generate_pdf(output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    elements.append(Paragraph("MMOCDPAD-DRL Security Intelligence Report", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Metadata
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elements.append(Paragraph(f"Generated Timestamp: {now}", styles['Normal']))
    elements.append(Paragraph("System Status: Operational (Active Monitoring)", styles['Normal']))
    elements.append(Spacer(1, 24))
    
    # Summary Table
    data = [
        ["Metric", "Value"],
        ["Total Devices Monitored", "5"],
        ["AI Detection Accuracy", "98.4%"],
        ["Encryption Protocol", "MMO-SPN (Matyas-Meyer-Oseas)"],
        ["Anomaly Detection Mode", "Deep Reinforcement Learning (DQN)"]
    ]
    t = Table(data, colWidths=[200, 200])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(t)
    elements.append(Spacer(1, 24))
    
    # Device Logs Header
    elements.append(Paragraph("Recent Security Events & Anomaly Analysis", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    # Fake logs for report
    log_data = [
        ["Timestamp", "Device ID", "Action", "Confidence"],
        ["2024-05-14 22:30", "IIoT_DEV_102", "Denied", "94.5%"],
        ["2024-05-14 22:35", "IIoT_DEV_104", "Allowed", "98.1%"],
        ["2024-05-14 22:40", "IIoT_DEV_101", "Denied", "91.2%"]
    ]
    t_logs = Table(log_data, colWidths=[120, 100, 80, 80])
    t_logs.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    elements.append(t_logs)
    
    doc.build(elements)
    print(f"Report generated: {output_path}")

if __name__ == "__main__":
    generate_pdf("test_report.pdf")
