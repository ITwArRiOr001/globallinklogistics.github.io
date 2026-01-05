# GOOGLE COLAB SPECIFIC
!pip install reportlab
from google.colab import drive
drive.mount('/content/drive')

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

pdf_filename = "/content/drive/MyDrive/IEC_Requirements_Guide_2026.pdf"
firm_name = "Global Link Logistics"  # CHANGE
website = "info@globallinklogistics-demo.com"  # CHANGE

def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor("#2E4053"))
    canvas.drawString(40, 30, f"Free resource by {firm_name} | {website} | Apply in 1–3 Days")
    canvas.restoreState()

doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=50, bottomMargin=80)
styles = getSampleStyleSheet()
styles['Title'].fontSize = 20
styles['Heading2'].fontSize = 14
styles['Normal'].fontSize = 10

story = []

# Cover (HS Code Style)
story.append(Paragraph("IEC Application Requirements Guide – Jan 2026", styles['Title']))
story.append(Spacer(1, 20))
story.append(Paragraph("Step-by-Step DGFT ANF-2A Guide | Avoid 70% Rejections", styles['Heading2']))
story.append(Spacer(1, 12))
story.append(Paragraph("Designed for First-Time Exporters, MSMEs & Students", styles['Normal']))
story.append(Spacer(1, 20))
story.append(Paragraph("Prepared by: Ayaan Khan<br/>BCA – UI/UX & Technology Specialization<br/>2026", styles['Italic']))
story.append(Spacer(1, 30))

story.append(Paragraph("""
<b>Note:</b> 2026 DGFT: 1–3 day processing with complete docs.
•Fee ₹500. Incomplete apps = 70% rejections (PAN mismatch main cause).<br/>
•Always verify at dgft.gov.in.<br/>
•Last updated: January 2026.
""", styles['Normal']))
story.append(Spacer(1, 30))

# How to Use / Instructions (HS Code Style)
story.append(Paragraph("<b>How to Apply for IEC</b>", styles['Heading2']))
story.append(Spacer(1, 12))
story.append(Paragraph("""
• HS Codes: 6-digit global standard for classifying goods (managed by World Customs Organization)<br/>
• Structure: First 2 digits = Chapter, next 2 = Heading, last 2 = Subheading<br/>
• Why accurate codes matter: Avoid delays, penalties & incorrect duties<br/>
• Refer chapters to classify goods accurately<br/>
• Avoid errors using “Common Mistakes” notes<br/>
• Trade Notes provide real-world examples
""", styles['Normal']))
story.append(Spacer(1, 20))

# Quick Tips Table (HS Code Style)
story.append(Paragraph("<b>Quick IEC Application Tips</b>", styles['Heading3']))
story.append(Spacer(1, 8))
tips_data = [["• Use DGFT portal only – no agents needed"], ["• Aadhaar eSign for individuals (free, 2 days faster)"], ["• Class 3 DSC for companies (₹2K, eMudhra)"]]
tips_table = Table(tips_data, colWidths=[500])
tips_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.lightgrey),
    ('BACKGROUND', (0,0), (-1,-1), colors.beige),
]))
story.append(tips_table)
story.append(Spacer(1, 20))

# Structure Illustration Table (HS Code Style – IEC Steps)
story.append(Paragraph("<b>IEC Application Structure at a Glance</b>", styles['Heading3']))
story.append(Spacer(1, 8))
structure_data = [
    ["Step 1: Register", "Create DGFT account with PAN/Email", "Tip: Enable 2FA"],
    ["Step 2: Fill ANF-2A", "Online form – upload docs", "Tip: Save draft"],
    ["Step 3: Pay Fee", "₹500 online", "Tip: Receipt auto-generated"],
    ["Step 4: eSign/DSC Submit", "Aadhaar or Class 3", "Tip: Individuals use eSign app"],
    ["Step 5: Track", "IEC issued in 1–3 days", "Tip: Check status daily"],
]

structure_table = Table(structure_data, colWidths=[120, 200, 180])
structure_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.grey),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
]))
story.append(structure_table)
story.append(Spacer(1, 40))

# Required Documents Table (HS Code Style – Index Table)
story.append(Paragraph("<b>Required Documents Index</b>", styles['Heading3']))
story.append(Spacer(1, 8))
docs_data = [
    ["Document", "Mandatory", "Notes (2026)"],
    ["PAN Card", "Yes", "Primary ID – match name exactly"],
    ["Aadhaar Card", "Yes (Individuals)", "For eSign – biometrics"],
    ["Bank Certificate", "Yes", "Cancelled cheque format"],
    ["Digital Signature (Class 3 DSC)", "Yes (Companies/LLP)", "Or Director Aadhaar"],
    ["GST Certificate", "Optional", "Speeds processing"],
    ["Address Proof", "Yes", "Utility bill <3 months old"],
    ["Passport Size Photo", "Yes", "4.5x3.5 cm JPEG"],
]

docs_table = Table(docs_data, colWidths=[140, 100, 260])
docs_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.lightgrey),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
]))
story.append(docs_table)
story.append(Spacer(1, 20))

# Step-by-Step Application Process (HS Code Directory Style – Clean Single Column)
story.append(Paragraph("<b>Step-by-Step Application Process (2026)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

steps_data = [
    ["Step 1: Register on DGFT Portal\n•Create account with PAN/Email\n•Tip: Enable 2FA for security"],
    ["Step 2: Fill ANF-2A Form\n•Online form – upload all required documents\n•Tip: Save draft if incomplete to avoid timeout"],
    ["Step 3: Pay Fee\n•Rs500 via online net banking/UPI\n•Tip: Receipt is auto-generated – save PDF copy"],
    ["Step 4: eSign or DSC Submit\n•Individuals: Use Aadhaar eSign app (free & faster)\n•Companies: Class 3 DSC required\n•Tip: eSign saves 1–2 days processing"],
    ["Step 5: Track Status\n•IEC issued in 1–3 days\n•Tip: Check daily at dgft.gov.in → IEC → Status"],
    ["Step 6: Annual Update\n•Free every April–June\n•Tip: Miss it = ₹1,000 penalty + IEC deactivation risk"],
]

steps_table = Table(steps_data, colWidths=[500])
steps_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEADING', (0,0), (-1,-1), 16),           # Increased line spacing for multi-line readability
    ('GRID', (0,0), (-1,-1), 1.0, colors.lightgrey),  # Subtle border
    ('BACKGROUND', (0,0), (-1,-1), colors.lightblue), # Matches HS Code "Quick Tips" style
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(steps_table)
story.append(Spacer(1, 30))

# Common Mistakes Table (HS Code Style – Top 20 Style)
story.append(Paragraph("<b>Common Mistakes (70% Rejections)</b>", styles['Heading3']))
story.append(Spacer(1, 8))
mistakes_data = [
    ["Mistake", "Impact", "Fix"],
    ["Wrong PAN name match", "Immediate rejection", "Double-check spelling"],
    ["Missing bank cert", "1-week delay", "Use cancelled cheque template"],
    ["No DSC for companies", "Manual verification", "Get Class 3 from eMudhra"],
    ["Old address proof", "Invalid", "Use <3 months old document"],
    ["No photo upload", "Incomplete", "4.5x3.5 cm JPEG"],
]

mistakes_table = Table(mistakes_data, colWidths=[140, 100, 260])
mistakes_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.lightgrey),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.whitesmoke]),
]))
story.append(mistakes_table)
story.append(Spacer(1, 20))

# Tips & FAQ (HS Code Style – Normal Text)
story.append(Paragraph("<b>Tips & FAQ (2026)</b>", styles['Heading3']))
story.append(Spacer(1, 8))
story.append(Paragraph("""
• FAQ: IEC valid lifetime? Yes – annual update free.<br/>
• Tip: Use DGFT's free helpdesk for queries (1800-111-123).<br/>
• FAQ: IEC for imports too? Yes – same form.<br/>
• Tip: MSMEs get priority processing (1 day).<br/>
• FAQ: Fee waiver? No – but online payment instant.
""", styles['Normal']))

doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)

print("✅IEC Requirements Guide PDF Generated!")
print(f"📄 {pdf_filename}")