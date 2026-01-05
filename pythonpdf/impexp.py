from google.colab import drive
drive.mount('/content/drive', force_remount=True)

!pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Image
import requests
from io import BytesIO
from reportlab.platypus import Image
# ====================== CONFIG ======================
pdf_filename = "/content/drive/MyDrive/Import_Export_Documentation_Checklist_2026.pdf"
firm_name = "Global Link Logistics"        # ← CHANGE THIS
website = "info@globallinklogistics-demo.com"     # ← CHANGE THIS

# ====================== FOOTER ======================
def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor("#2E4053"))
    footer_text = f"Free resource by {firm_name} | Helping exporters navigate global trade | Visit {website} for consultations"
    canvas.drawString(40, 30, footer_text)
    canvas.restoreState()

# ====================== SETUP ======================
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    rightMargin=40, leftMargin=40,
    topMargin=50, bottomMargin=80
)
styles = getSampleStyleSheet()
styles['Title'].fontSize = 20
styles['Title'].leading = 24
styles['Heading2'].fontSize = 14
styles['Heading2'].spaceAfter = 12

story = []

# ====================== COVER ======================
story.append(Paragraph("Import–Export Documentation Checklist – 2026", styles['Title']))
story.append(Spacer(1, 40))

story.append(Paragraph("A step-by-step guide to essential documents in international trade", styles['Heading2']))
story.append(Spacer(1, 42))

story.append(Paragraph("Designed for First-Time Exporters, Students & Trade Professionals", styles['Normal']))
story.append(Spacer(1, 40))

story.append(Paragraph("Prepared by: Ayaan Khan<br/>BCA – UI/UX & Technology Specialization<br/>2026", styles['Italic']))
story.append(Spacer(1, 60))

story.append(Paragraph("""
<b>Note:</b> This checklist covers standard documents for general merchandise trade.
Requirements may vary by country, product, and Incoterms. Always consult official sources and your freight forwarder.
""", styles['Normal']))
story.append(Spacer(1, 100))

# ====================== SECTIONS ======================
def section_title(title):
    story.append(Paragraph(title, styles['Heading2']))
    story.append(Spacer(1, 22))

def checklist_table(items):
    data = [["", item] for item in items]
    table = Table(data, colWidths=[30, 460])
    table.setStyle(TableStyle([
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 11),
        ('LEFTPADDING', (1,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('BACKGROUND', (0,0), (-1,-1), colors.whitesmoke),
    ]))
    story.append(table)
    story.append(Spacer(1, 50))

# Pre-Shipment
section_title("1. Pre-Shipment Documents")
checklist_table([
    "Importer Exporter Code (IEC) from DGFT",
    "GST Registration & LUT filing (for zero-rated exports)",
    "RCMC (Registration-cum-Membership Certificate) if required",
    "Commercial Invoice (signed & stamped)",
    "Packing List (detailed weight, dimensions, packages)",
    "Purchase Order / Contract from buyer",
    "Proforma Invoice (if advance payment)",
    "Letter of Credit (if payment via LC)",
    "Export Order Confirmation",
    "AD Code Registration with Bank",
])

# Shipment
section_title("2. Shipping & Transport Documents")
checklist_table([
    "Shipping Bill (filed via ICEGATE)",
    "Bill of Lading (Original + copies) or Airway Bill",
    "Marine Insurance Policy / Certificate",
    "Certificate of Origin (GSP/Form A/India-UAE CEPA etc.)",
    "Phytosanitary Certificate (for agri products)",
    "Health Certificate (for food/animal products)",
    "Fumigation Certificate (wooden packaging)",
    "SDF Form (Shipping Bill Declaration)",
    "GR Waiver (if applicable)",
    "Mate’s Receipt (from shipping line)",
])

# Post-Shipment
section_title("3. Post-Shipment & Payment Documents")
checklist_table([
    "Bank Realization Certificate (BRC/e-BRC)",
    "Bill of Exchange (for DP/DA payment)",
    "Export Invoice with EGM details",
    "Customs Certified Shipping Bill copy",
    "Proof of Export (ARE-1 if excise applicable)",
    "Duty Drawback / RoDTEP claim filing",
    "IGST Refund claim (if applicable)",
    "Foreign Inward Remittance Certificate (FIRC)",
    "Advance Authorization closure (if used)",
])

# Common Dock Delays & Prevention (Improved Alignment)
story.append(PageBreak())
section_title("Common Dock Delays & How to Prevent Them")
story.append(Paragraph("Understanding triggers helps you plan better and save costs.", styles['Normal']))
story.append(Spacer(1, 12))

delays_data = [
    ["Delay Trigger", "Typical Impact", "Prevention Tip"],
    ["Document mismatch", "Full examination → 3–7 days hold", "Triple-check alignment before filing"],
    ["Risk profiling flag", "Physical scan → detention charges", "Use experienced CHA for smooth clearance"],
    ["Late Shipping Bill filing", "No Let Export → container left behind", "File early—monitor ICEGATE status"],
    ["Vessel delay (carrier side)", "Extra storage (sometimes free)", "Choose reliable shipping lines"],
    ["Missing certificates (Phyto/Health)", "Seizure or return", "Prepare product-specific docs in advance"],
]

delays_table = Table(delays_data, colWidths=[150, 170, 170])
delays_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),      # Center headers
    ('ALIGN', (0,1), (-1,-1), 'LEFT'),       # Left-align content
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 1, colors.grey),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('WORDWRAP', (0,0), (-1,-1), True),      # Enable wrap (ReportLab supports via style)
]))
story.append(delays_table)
story.append(Spacer(1, 20))

# Pro Tips (Expanded with Dock Focus)
section_title("Pro Tips to Avoid Dock Delays & Costs")
checklist_table([
    "File Shipping Bill BEFORE vessel departure (ideally 48–72 hours early)",
    "Match Invoice, Packing List & Shipping Bill exactly (HS code, value, description)",
    "Use correct HS Code & Incoterms—common trigger for examinations",
    "Plan carting 3–5 days before vessel ETA to buffer delays",
    "Track Shipping Bill status daily on ICEGATE for Let Export Order",
    "Keep digital + physical copies of all docs at dock",
    "Consult licensed CHA for high-risk shipments (e.g., restricted goods)",
    "If examined: Expect demurrage—negotiate storage waiver with line",
    "Missed vessel? Rollover fees + 7–14 day delay—always confirm ETD/ETA",
])

# Critical Timeline (Improved Alignment)
section_title("Critical Timeline: Dock Entry to Vessel Onboarding")
story.append(Paragraph("Avoid customs holds, examinations & missed sailings—plan ahead to prevent demurrage & rollover costs.", styles['Normal']))
story.append(Spacer(1, 12))

flow_data = [
    ["Stage", "Key Document/Action", "Recommended Timeline", "Risk & Cost if Delayed"],
    ["Goods Reach Dock/CFS", "Carting Order + Full Docs Ready", "3–5d before vessel cut", "Demurrage starts (~₹5,000–15,000/day)"],
    ["Customs Verification", "Shipping Bill Filed + All Supporting", "File early via ICEGATE", "Mismatch → Hold → Physical Examination"],
    ["Examination (if flagged)", "Officer Physical Check", "Random/risk-based (1–7d)", "Detention charges + delay buildup"],
    ["Let Export Order (LEO)", "Customs Approval Stamp", "Must before loading", "No LEO → Container not loaded"],
    ["Container Loading", "Preventive Officer Supervision", "Before vessel sails", "Missed → Rollover (7–14 days late + fees)"],
    ["Shipped on Board", "Mate’s Receipt + EGM Filing", "Post-sailing by carrier", "No EGM → No drawback/refunds"],
]

flow_table = Table(flow_data, colWidths=[120, 160, 110, 140])
flow_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9.5),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('ALIGN', (0,1), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
]))
story.append(flow_table)
story.append(Spacer(1, 20))

# 1. Define the URL and a browser-like header
img_url = "https://www.slideteam.net/wp/wp-content/uploads/2022/11/Shipping-Process-Flow-from-Order-Management-to-Customer-.png"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
try:
    # 2. Download the image manually with the header
    response = requests.get(img_url, headers=headers)
    response.raise_for_status()  # Check if the download was successful

    # 3. Create an in-memory image file (BytesIO) from the downloaded content
    img_data = BytesIO(response.content)

    # 4. Create the ReportLab Image object using the in-memory data
    # Adjust width/height as needed to fit your PDF page
    process_flow_img = Image(img_data, width=450, height=300)

    # 5. Add to your story
    story.append(process_flow_img)
    story.append(Spacer(1, 40))

    print("✅ Image downloaded and added successfully.")

except Exception as e:
    print(f"❌ Failed to add image: {e}")
    # Optional: Add a placeholder text if image fails
    story.append(Paragraph(f"Image could not be loaded: {img_url}", styles['Normal']))
    story.append(Spacer(1, 10))
story.append(Paragraph("<b>Visual Summary:</b> INTERNATIONAL CARGO EXPRESS SHIPPING TIMELINE", styles['Heading3']))
story.append(Paragraph("Source: Professional logistics illustration | Always verify processes with your CHA/freight forwarder.", styles['Normal']))
story.append(Spacer(1, 20))

# 1. Define the URL and a browser-like header
img_url = "https://icecargo.com.au/wp-content/uploads/2022/10/Shipping-Timeline-1.jpg-1.webp"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
try:
    # 2. Download the image manually with the header
    response = requests.get(img_url, headers=headers)
    response.raise_for_status()  # Check if the download was successful

    # 3. Create an in-memory image file (BytesIO) from the downloaded content
    img_data = BytesIO(response.content)

    # 4. Create the ReportLab Image object using the in-memory data
    # Adjust width/height as needed to fit your PDF page
    process_flow_img = Image(img_data, width=450, height=300)

    # 5. Add to your story
    story.append(process_flow_img)
    story.append(Spacer(1, 40))

    print("✅ Image downloaded and added successfully.")

except Exception as e:
    print(f"❌ Failed to add image: {e}")
    # Optional: Add a placeholder text if image fails
    story.append(Paragraph(f"Image could not be loaded: {img_url}", styles['Normal']))
    story.append(Spacer(1, 10))
story.append(Paragraph("<b>Visual Summary:</b> Export Journey from Factory to Vessel Onboarding", styles['Heading3']))
story.append(Paragraph("Source: Professional logistics illustration | Always verify processes with your CHA/freight forwarder.", styles['Normal']))
story.append(Spacer(1, 20))

# ====================== BUILD ======================
doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)

print("✅ Import-Export Documentation Checklist PDF Generated!")
print(f"📄 Saved at: {pdf_filename}")