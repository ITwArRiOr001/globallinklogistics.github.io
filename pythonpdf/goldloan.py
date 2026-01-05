!pip install reportlab requests Pillow
from google.colab import drive

# Ensure Drive is mounted
drive.mount('/content/drive', force_remount=True)

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import requests
from io import BytesIO

# ====================== CONFIG ======================
pdf_filename = "/content/drive/MyDrive/Gold_Loan_vs_Bank_Loan_Comparison_2026.pdf"
firm_name = "Global Link Logistics"        # ← CHANGE THIS
website = "info@globallinklogistics-demo.com"
# ====================== FOOTER ======================
def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor("#2E4053"))
    footer_text = f"Free resource by {firm_name} | Helping exporters navigate global trade | Visit {website} for consultations"
    canvas.drawString(40, 30, footer_text)
    canvas.restoreState()

# ====================== SETUP ======================
doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=50, bottomMargin=80)
styles = getSampleStyleSheet()
styles['Title'].fontSize = 20
styles['Title'].leading = 24
styles['Heading2'].fontSize = 14
styles['Heading2'].spaceAfter = 12

story = []

# ====================== COVER ======================
story.append(Paragraph("Gold Loan vs Bank Loan Comparison – 2026", styles['Title']))
story.append(Spacer(1, 20))
story.append(Paragraph("Quick working capital guide for exporters & businesses", styles['Heading2']))
story.append(Spacer(1, 12))
story.append(Paragraph("Designed for Exporters, MSMEs, Students & Trade Finance Professionals", styles['Normal']))
story.append(Spacer(1, 20))
story.append(Paragraph("Prepared by: Ayaan Khan<br/>BCA – UI/UX & Technology Specialization<br/>2026", styles['Italic']))
story.append(Spacer(1, 30))

story.append(Paragraph("""
<b>Note:</b> Rates indicative as of January 2026 (RBI, SBI, HDFC, Muthoot data). /n
Gold loans: 8.5%–12% p.a. |/n Bank business loans: 10.5%–16%+ p.a.<br/>
From April 2026: RBI tiered LTV up to 85% for loans ≤₹2.5 lakh.<br/>
Always check latest offers with lenders.
""", styles['Normal']))
story.append(Spacer(1, 90))

# ====================== QUICK COMPARISON TABLE (Updated Rates) ======================
story.append(Paragraph("<b>Quick Comparison at a Glance</b>", styles['Heading2']))
story.append(Spacer(1, 22))

comparison_data = [
    ["Parameter", "Gold Loan", "Bank Loan (Business/Overdraft)"],
    ["Interest Rate (Jan 2026)", "8.5% – 12% p.a.", "10.5% – 16%+ p.a."],
    ["Processing Time", "Same day / 1–2 hours", "7–30 days"],
    ["Loan Amount", "75–85% of gold value (tiered from Apr 2026)", "Based on turnover/credit score"],
    ["Collateral", "Gold jewellery/coins (18–22K)", "Property or unsecured (higher rate)"],
    ["Documentation", "Minimal (KYC + valuation)", "Extensive (ITR, financials)"],
    ["Tenure", "3–36 months (bullet option)", "1–7 years"],
    ["Prepayment Charges", "Usually nil", "1–4% in early years"],
    ["Best For Exporters", "Urgent orders, LC margins", "Large expansion projects"],
]

comp_table = Table(comparison_data, colWidths=[160, 170, 170])
comp_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('ALIGN', (0,1), (-1,-1), 'LEFT'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(comp_table)
story.append(Spacer(1, 30))

# TOP LENDERS TABLE (Unique Data)
story.append(PageBreak())
story.append(Paragraph("<b>Top Gold Loan Lenders (Jan 2026 Rates)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

lenders_data = [
    ["Lender", "Starting Rate", "Max LTV", "Notes"],
    ["SBI", "8.25%", "75–85%", "Lowest bank rate"],
    ["HDFC Bank", "9.30%", "75–85%", "Quick digital"],
    ["Muthoot Finance", "11–12%", "Up to 85%", "Wide branches"],
    ["Manappuram", "10–12%", "Up to 85%", "Bullet option"],
    ["Bajaj Finance", "9.50%", "Up to 85%", "Online process"],
]

lenders_table = Table(lenders_data, colWidths=[140, 120, 120, 160])
lenders_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")), ('TEXTCOLOR', (0,0), (-1,0), colors.white), ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey), ('BACKGROUND', (0,1), (-1,-1), colors.beige)]))
story.append(lenders_table)
story.append(Spacer(1, 20))

# ====================== DETAILED BREAKDOWN (Empathetic) ======================
story.append(Paragraph("<b>Why Gold Loan is Often Best for Exporters</b>", styles['Heading2']))
story.append(Spacer(1, 8))
story.append(Paragraph("""
• <b>Speed Saves Deals:</b> Funds in hours — perfect for urgent buyer advances or LC margins<br/>
• <b>Lower Cost:</b> Secured by gold → 2–4% cheaper than unsecured bank loans<br/>
• <b>No Income Proof Hassle:</b> Based on gold value, not turnover/ITR<br/>
• <b>Cashflow Friendly:</b> Pay interest monthly, principal at end (bullet repayment)<br/>
• <b>No End-Use Rules:</b> Flexible for raw materials, freight, or working capital<br/>
• <b>RBI protects: Auction only after 30-day notice (2026 rules) </b>
""", styles['Normal']))
story.append(Spacer(1, 15))

story.append(Paragraph("<b>Risks & Tips</b>", styles['Heading2']))
story.append(Paragraph("""
• Gold price fall → Margin call possible<br/>
• Prepay freely (most lenders)<br/>
• Choose RBI-regulated lenders only<br/>
• Use for business? No end-use check in gold loans
""", styles['Normal']))
story.append(Spacer(1, 20))

story.append(Paragraph("<b>When Traditional Bank Loan Makes Sense</b>", styles['Heading2']))
story.append(Spacer(1, 8))
story.append(Paragraph("""
• Need ₹50 lakh+ for machinery/factory<br/>
• Longer tenure (5–7 years) required<br/>
• Building strong credit history for future large loans<br/>
• Eligible for government schemes (ECLGS, Mudra, PMEGP subsidies)
""", styles['Normal']))
story.append(Spacer(1, 15))

# ====================== RECOMMENDATION TABLE ======================
story.append(Paragraph("<b>2026 Recommendation for Exporters</b>", styles['Heading2']))
story.append(Spacer(1, 12))

rec_data = [
    ["Scenario", "Recommended", "Why It Wins"],
    ["Urgent export order / LC margin", "Gold Loan", "Speed & low stress"],
    ["Short-cycle raw material purchase", "Gold Loan", "Cheaper + bullet repayment"],
    ["Factory expansion / heavy machinery", "Bank Loan", "Higher amount + long tenure"],
    ["Building long-term banking relationship", "Bank Loan", "Improves future credit access"],
]

rec_table = Table(rec_data, colWidths=[170, 140, 190])
rec_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
]))
story.append(rec_table)
story.append(Spacer(1, 40))

def add_image_to_story(url, story):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # FIX: Use BytesIO directly, NOT ImageReader
        img_data = BytesIO(response.content)

        # Create Image object (adjust width/height for your PDF)
        img = Image(img_data, width=400, height=225)
        img.hAlign = 'CENTER'
        story.append(img)
        print(f"✅ Success: {url}")

    except Exception as e:
        # Fallback: If image fails, add a text note so the PDF doesn't crash
        print(f"❌ Failed: {url} → {e}")
        styles = getSampleStyleSheet()
        story.append(Spacer(1, 20))
        story.append(Paragraph(f"<i>(Graphic omitted: {url})</i>", styles['Normal']))

# Example usage in your loop:
image_urls = [
    "https://images.verifiedmarketresearch.com/assets/Gold-Loan-Market-Size-And-Forecast.jpg",
    "https://www.thebusinessresearchcompany.com/graphimages/personal_loans_market_report_graphname.webp",
    "https://www.slideteam.net/media/catalog/product/cache/1280x720/5/_/5_types_of_bank_loan_services_slide01.jpg",
    "https://img.etimg.com/thumb/width-1600,height-900,imgsize-552284,resizemode-75,msid-125325608/wealth/borrow/gold-loan-repayment-which-method-saves-you-the-most-money-a-simple-guide-for-every-borrower.jpg",
    "https://images.verifiedmarketresearch.com/assets/Global-Gold-Loan-Market-Segmentation-Analysis.jpg",
]
for url in image_urls:
    add_image_to_story(url, story)


# ====================== BUILD ======================
doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)

print("✅ Gold Loan vs Bank Loan Comparison PDF Generated Successfully!")
print(f"📄 Saved at: {pdf_filename}")
print("Professional, empathetic, accurate rates (Jan 2026), robust image loading.")