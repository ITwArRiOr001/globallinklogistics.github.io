
!pip install reportlab requests
from google.colab import drive
import os

# 1. Mount the Drive
drive.mount('/content/drive', force_remount=True)

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import requests
from io import BytesIO

pdf_filename = "/content/drive/MyDrive/Cold_Chain_Guide_Perishables_2026.pdf"
firm_name = "Global Link Logistics"  # CHANGE
website = "info@globallinklogistics-demo.com"  # CHANGE

def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor("#2E4053"))
    canvas.drawString(40, 30, f"Free resource by {firm_name} | {website} | Global Cold Chain $366B 2026")
    canvas.restoreState()

doc = SimpleDocTemplate(pdf_filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=50, bottomMargin=80)
styles = getSampleStyleSheet()
styles['Title'].fontSize = 20
styles['Heading2'].fontSize = 14
styles['Normal'].fontSize = 10

story = []

# COVER (Professional Hook)
story.append(Paragraph("Ultimate Cold Chain Export Guide: Perishables – January 2026", styles['Title']))
story.append(Spacer(1, 20))
story.append(Paragraph("APEDA/UN Insights: Global Market $366.8 Billion | Save ₹50K/T Spoilage", styles['Heading2']))
story.append(Spacer(1, 12))
story.append(Paragraph("For Exporters, Logistics Pros & Beginners", styles['Normal']))
story.append(Spacer(1, 20))
story.append(Paragraph("Prepared by: Ayaan Khan | BCA UI/UX & Technology Specialization | 2026", styles['Italic']))
story.append(Spacer(1, 30))

story.append(Paragraph("""
<b>Key Insight:</b> 40% perishables lost in transit globally ($150B annual loss – UN 2026).<br/>
India exports: $15B potential | UAE QR mandatory | U.S. $11B frozen demand.<br/>
This guide delivers 40+ professional insights to protect your profits.
""", styles['Normal']))
story.append(Spacer(1, 30))

# Global Loss Stats (Shocking Data – After Cover)
story.append(Paragraph("<b>Global & India Cold Chain Losses (UN/APEDA 2026)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

loss_data = [
    ["Region", "Loss %", "Annual Value", "Key Insight"],
    ["Global", "40%", "$150 Billion", "Fruits/veggies/seafood waste"],
    ["India", "30–40%", "₹92,000 Crore", "Highest in bananas/mangoes"],
    ["Banana Export", "20–30%", "₹40–60K per 20T container", "Bruising/spoilage main cause"],
]

loss_table = Table(loss_data, colWidths=[100, 80, 120, 200])
loss_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.grey),
    ('BACKGROUND', (0,1), (-1,-1), colors.lightcoral),  # Red urgency
]))
story.append(loss_table)
story.append(Spacer(1, 30))

# PACKAGING & TECH (10 Items)
story.append(Paragraph("<b>Packaging & Tech Essentials (APEDA 2026)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

pack_data = [
    ["Essential", "Benefit (2026 Insight)"],
    ["Ventilated cartons (5–10% holes)", "40% better airflow"],
    ["Ethylene absorbers", "Extends shelf 7–10 days"],
    ["QR traceability labels", "Gulf mandatory – faster clearance"],
    ["Temperature data loggers", "Proof for insurance claims"],
    ["Solar-powered reefers", "₹10L India grant – 30% energy save"],
    ["IoT sensors", "Real-time alerts – 25% less loss"],
    ["Biodegradable liners", "EU green compliance"],
    ["Shock absorbers", "Reduce bruising 35%"],
    ["Multi-layer insulation", "Stable temp in heat"],
    ["Fumigation + cert", "Wooden crate compliance"],
]

pack_table = Table(pack_data, colWidths=[200, 300])
pack_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
]))
story.append(pack_table)
story.append(Spacer(1, 30))

# TEMP TABLE (15 Products – Professional)
story.append(Paragraph("<b>Optimal Temperatures (APEDA 2026 – 15 Key Products)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

temp_data = [
    ["Product", "Pre-Cool (°C)", "Transit (°C)", "Shelf Life (Days)", "Risk & Cost if Wrong"],
    ["Bananas", "13–15", "13–14", "21–28", "Bruising >15°C (₹50K/T loss)"],
    ["Mangoes", "10–13", "11–13", "14–21", "Chilling injury <10°C"],
    ["Grapes", "0–1", "0", "30–60", "Mold >5°C (30% waste)"],
    ["Apples", "0–2", "0–1", "60–90", "Rot >4°C"],
    ["Oranges", "3–5", "4–6", "30–45", "Dehydration <3°C"],
    ["Shrimp", "-18", "-18", "90+", "Bacterial >-15°C (full rejection)"],
    ["Salmon", "0", "0–2", "14–21", "Spoilage >4°C ($5K/T)"],
    ["Cherries", "-1–0", "-1", "14–21", "Cracking >2°C"],
    ["Avocados", "5–8", "5–7", "21–28", "Black spots <5°C"],
    ["Tomatoes", "10–13", "10–12", "14–21", "Chilling injury <10°C"],
    ["Lettuce", "0", "0–1", "7–14", "Browning >5°C"],
    ["Berries", "0", "0", "7–10", "Mold >2°C (40% loss)"],
    ["Asparagus", "2–4", "2–3", "14–21", "Yellowing >6°C"],
    ["Seafood Mix", "-18", "-18", "60–90", "Unsafe thaw >-15°C"],
    ["Kiwi", "0–1", "0", "60–90", "Softening >4°C"],
]

temp_table = Table(temp_data, colWidths=[100, 80, 80, 90, 150])
temp_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('GRID', (0,0), (-1,-1), 1.0, colors.grey),  # Thicker professional borders
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('ALIGN', (0,1), (-1,-1), 'LEFT'),
]))
story.append(temp_table)
story.append(Spacer(1, 30))

# Top 10 Challenges & Solutions
story.append(Paragraph("<b>Top 10 Exporter Challenges & Solutions (2026)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

challenge_data = [
    ["Challenge", "Impact", "Solution"],
    ["Reefer shortage (+15% demand)", "Delayed shipments", "Book 4 weeks early + solar reefers"],
    ["High energy cost", "30% margin loss", "₹10L India solar grant"],
    ["Temperature deviation", "40% spoilage", "IoT sensors + alerts"],
    ["QR compliance (Gulf)", "Customs hold", "Add traceability labels"],
    ["Carbon tax (EU)", "Extra duty", "Electric reefers"],
    ["Insurance gaps", "No claim on spoilage", "Add cold chain cover"],
    ["Port congestion", "7-day delay", "Multi-modal (air backup)"],
    ["Data logger cost", "No proof", "₹5K smart stickers"],
    ["Training gap", "Non-compliance", "APEDA courses"],
    ["Forecasting error", "Over/under stock", "AI predictive tools"],
]

challenge_table = Table(challenge_data, colWidths=[150, 150, 200])
challenge_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.grey),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
]))
story.append(challenge_table)
story.append(Spacer(1, 80))

# TOP MARKETS (10 Countries – Shocking Demand)
story.append(Paragraph("<b>Top 10 Import Markets (UN Comtrade 2026 – $366B Global)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

market_data = [
    ["Country", "Key Product Demand", "2026 Value", "Requirement"],
    ["U.S.", "Frozen fruits/seafood", "$11B", "FDA + -18°C strict"],
    ["UAE", "Bananas/mangoes", "$2.5B", "QR traceability mandatory"],
    ["Saudi Arabia", "Fruits/veggies", "$1.8B", "SASO + solar reefers"],
    ["China", "Shrimp/salmon", "$5B", "HACCP + ethylene-free"],
    ["EU (Germany)", "Grapes/apples", "$2B", "Organic + blockchain"],
    ["Japan", "Cherries/berries", "$1B", "JAS organic"],
    ["UK", "Mixed perishables", "$1.5B", "Post-Brexit labels"],
    ["Singapore", "Seafood", "$600M", "Halal + -18°C"],
    ["Netherlands", "Flowers/veggies", "$1B", "Greenhouse standards"],
    ["Australia", "Avocados", "$500M", "Biosecurity checks"],
]

market_table = Table(market_data, colWidths=[100, 140, 100, 160])
market_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.lightcyan),
]))
story.append(market_table)
story.append(Spacer(1, 30))

# BEST SOURCES (10 Origins)
story.append(Paragraph("<b>Best Sources Worldwide (2026 – Low Loss Leaders)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

source_data = [
    ["Product", "Top Origin", "Why Superior", "Volume"],
    ["Bananas", "Ecuador", "Year-round + 98% quality", "$2B"],
    ["Mangoes", "India", "Variety + APEDA support", "$1.5B"],
    ["Grapes/Cherries", "Chile", "IoT + 30% less loss", "$1.5B"],
    ["Apples", "Turkey", "EU-compliant tech", "$1.8B"],
    ["Shrimp", "Vietnam", "Cold chain leader", "$8B"],
    ["Salmon", "Norway", "Sustainable -18°C", "$7B"],
    ["Avocados", "Mexico", "Hass + stable supply", "$4B"],
]

source_table = Table(source_data, colWidths=[100, 120, 180, 100])
source_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.lightyellow),
]))
story.append(source_table)
story.append(Spacer(1, 30))

# Ultimate 2026 Adaptations & Trends (Detailed, Shocking Data)
story.append(PageBreak())
story.append(Paragraph("<b>2026 Cold Chain Adaptations & Future Trends</b>", styles['Title']))
story.append(Spacer(1, 20))
story.append(Paragraph("Global market: $366.8 Billion | India growth: 15–20% CAGR | Adopt now to stay ahead", styles['Heading2']))
story.append(Spacer(1, 12))

# Shocking Intro Stats
story.append(Paragraph("• Global cold chain: $366.8B (2026) – 30% growth from 2025 (Grand View Research)", styles['Normal']))
story.append(Paragraph("• 40% perishables lost annually = $150B waste (UN 2026)", styles['Normal']))
story.append(Paragraph("• India potential: $15B exports | Current loss: ₹92,000 Cr due to poor chain", styles['Normal']))
story.append(Paragraph("<b>Act in 2026: Future-Proof Your Cold Chain</b>", styles['Heading2']))
story.append(Spacer(1, 8))
story.append(Paragraph("Start with solar/IoT → Save ₹10–20L/year while meeting global standards. Your profit depends on it.", styles['Normal']))
story.append(Spacer(1, 20))

# Detailed Trends Table (Professional Boxed)
trends_data = [
    ["Trend", "2026 Insight & Data", "Exporter Benefit & ROI"],
    ["Solar-Powered Reefers", "₹10L APEDA grant per unit | 30% energy cost reduction", "Save ₹3–5L/year per container | 3-year payback"],
    ["IoT & Real-Time Sensors", "₹5L investment → 25–30% spoilage reduction (APEDA cases)", "Save ₹10–15L/year | 200% ROI in 3 years"],
    ["Blockchain Traceability", "Mandatory UAE/Saudi QR | EU demand rising", "+10–15% premium pricing | Faster customs (2 days saved)"],
    ["AI Predictive Maintenance", "25% less reefer downtime (Maersk 2026 pilot)", "Avoid ₹2L delay losses per shipment"],
    ["Electric Reefers", "EU carbon tax avoidance (2026 enforcement)", "Zero emission premium + 20% lower operating cost"],
    ["5G Real-Time Tracking", "98% arrival quality (Chile cherry exporters)", "Reduce insurance claims 40%"],
    ["Biodegradable Packaging", "EU Green Deal compliance | 10% carbon tax saving", "Access premium markets (Germany/Netherlands)"],
    ["Multi-Modal (Sea + Air)", "For high-value shrimp/salmon", "Cut transit time 3–5 days | Higher freshness premium"],
    ["Smart Data Loggers", "₹50K/unit with cloud upload", "Proof for $5K insurance claims | 90% recovery rate"],
    ["Green Certification", "APEDA organic + carbon-neutral label", "+20% price in EU/Japan markets"],
]

trends_table = Table(trends_data, colWidths=[100, 210, 220])
trends_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7.5),
    ('GRID', (0,0), (-1,-1), 1.0, colors.grey),  # Thick professional borders
    ('BACKGROUND', (0,1), (-1,-1), colors.lightcyan),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('ALIGN', (0,1), (-1,-1), 'LEFT'),
]))
story.append(trends_table)
story.append(Spacer(1, 30))

# Best Reefer Lines 2026
story.append(Paragraph("<b>Best Reefer Shipping Lines 2026 (Reliability & Tech Rating)</b>", styles['Heading2']))
story.append(Spacer(1, 12))

lines_data = [
    ["Line", "Fleet Size", "Tech Strength", "Reliability Score"],
    ["Maersk", "700+ reefers", "IoT + AI predictive", "98% on-time"],
    ["MSC", "800+ reefers", "Largest capacity", "96% reliability"],
    ["Hapag-Lloyd", "500+ reefers", "Solar pilot + blockchain", "95% eco-score"],
    ["CMA CGM", "600+ reefers", "Electric trials", "94% coverage"],
    ["ONE", "400+ reefers", "5G tracking", "93% Asia focus"],
]

lines_table = Table(lines_data, colWidths=[100, 100, 180, 120])
lines_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 1.0, colors.grey),
    ('BACKGROUND', (0,1), (-1,-1), colors.lightyellow),
]))
story.append(lines_table)
story.append(Spacer(1, 10))

# VISUAL (Professional Market Image)
story.append(Spacer(1, 10))

image_urls = [
    "https://shipglobal.in/wp-content/uploads/2025/02/cold-chain-info.png",
    "https://cdn.gminsights.com/image/rd/automotive-and-transportation/cold-chain-logistics-market-by-service-2025-2034.webp",
    "https://www.educba.com/academy/wp-content/uploads/2025/06/What-is-Cold-Chain-Logistics-.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ6smORLEqML_dLTCw-sTRu6yr87PPBmUo1azHb27N2RUNoOK-cJclGvmC&s=10",
]

headers = {"User-Agent": "Mozilla/5.0"}
img_added = False

for url in image_urls:
    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        img = Image(BytesIO(r.content), width=500, height=300)
        img.hAlign = 'CENTER'
        story.append(img)
        story.append(Spacer(1, 20))  # Optional: space between multiple images
        img_added = True
    except Exception as e:  # Good to catch and optionally log the error
        print(f"Failed to load image {url}: {e}")
        continue  # Skip failed ones and try the next

if not img_added:
    story.append(Paragraph("<b>Visual: $366.8B Global Cold Chain Market 2026</b>", styles['Heading3']))

doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)

print("✅ Ultimate Professional Cold Chain Guide Generated!")
print(f"📄 {pdf_filename}")
print("Data-rich, shocking stats, perfect UI—ready to impress!")