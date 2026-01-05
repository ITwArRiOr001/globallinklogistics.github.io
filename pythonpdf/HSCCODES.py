!pip install reportlab
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import KeepTogether, HRFlowable
from reportlab.lib import colors
from google.colab import drive
import os

# 1. MOUNT GOOGLE DRIVE
drive.mount('/content/drive')

# 2. SETUP PATH AND DOC
pdf_filename = "/content/drive/MyDrive/HS_Code_Directory_2026.pdf"
hs_chapters = {
"01": {
"title": "Live Animals",
"common_mistakes": "Distinguish breeding vs. non-breeding animals; live vs. slaughtered.",
"codes": [
("010121", "Pure-bred breeding horses", "Racing and equestrian sports"),
("010129", "Other live horses", "Transport and recreation"),
("010221", "Pure-bred breeding cattle", "Dairy and beef farming"),
("010229", "Other live cattle", "Meat production"),
("010310", "Pure-bred breeding swine", "Commercial pig farming"),
("010391", "Live swine <50kg", "Feeder pigs"),
("010420", "Live goats", "Meat and milk production"),
("010511", "Live fowls (chickens) ≤185g", "Day-old chicks for poultry"),
("010594", "Live fowls (chickens) >185g", "Broiler chickens"),
("010599", "Other live poultry", "Turkeys/ducks"),
]
},
"02": {
"title": "Meat and Edible Meat Offal",
"common_mistakes": "Fresh/chilled vs. frozen; cuts vs. carcasses.",
"codes": [
("020130", "Boneless bovine meat, fresh or chilled", "Premium beef cuts"),
("020230", "Boneless bovine meat, frozen", "Global beef trade staple"),
("020312", "Hams and shoulders, swine, bone-in", "Processed pork"),
("020329", "Other swine meat, frozen", "Pork shoulders/legs"),
("020714", "Chicken cuts and offal, frozen", "Major poultry export"),
("020727", "Turkey cuts, frozen", "Holiday demand"),
("021011", "Hams, swine, cured", "Processed meats"),
]
},
"03": {
"title": "Fish and Crustaceans, Molluscs",
"common_mistakes": "Fresh vs. frozen fillets; farmed vs. wild.",
"codes": [
("030214", "Atlantic salmon, fresh or chilled", "Premium seafood"),
("030471", "Cod fillets, frozen", "White fish staple"),
("030617", "Other shrimps and prawns, frozen", "High-volume shrimp trade"),
("030743", "Cuttle fish and squid, frozen", "Seafood delicacy"),
("030389", "Other fish fillets, frozen", "Tuna/pollock alternatives"),
("030499", "Fish meat, minced", "Surimi base"),
("030614", "Crabs, frozen", "Shellfish trade"),
]
},
"04": {
"title": "Dairy Produce; Birds' Eggs; Natural Honey",
"common_mistakes": "Processed cheese vs. natural; in-shell eggs vs. liquid.",
"codes": [
("040510", "Butter", "Dairy fat export"),
("040690", "Cheese (other than fresh/processed)", "Cheddar/edam varieties"),
("040721", "Birds' eggs, in shell", "Table eggs"),
("040811", "Egg yolks, dried", "Bakery ingredient"),
("040900", "Natural honey", "Health food demand"),
("040610", "Fresh cheese (including whey cheese)", "Mozzarella/ricotta"),
]
},
"08": {
"title": "Edible Fruit and Nuts;",
"common_mistakes": "Fresh vs. dried; nuts in shell vs. shelled.",
"codes": [
("080310", "Plantains, fresh", "Tropical staple"),
("080390", "Bananas, fresh", "World's top fruit export"),
("080410", "Dates, fresh or dried", "Middle East specialty"),
("080510", "Oranges, fresh", "Citrus leader"),
("080520", "Mandarins/tangerines", "Easy-peel varieties"),
("080610", "Grapes, fresh", "Table grapes"),
("080710", "Melons", "Seasonal fruit"),
("080810", "Apples, fresh", "Major temperate fruit"),
("081010", "Strawberries, fresh", "Berry trade"),
("080910", "Apricots, fresh", "Stone fruit"),
]
},
"09": {
"title": "Coffee, Tea, Maté and Spices",
"common_mistakes": "Roasted vs. unroasted coffee; whole vs. ground spices.",
"codes": [
("090111", "Coffee, not roasted, not decaffeinated", "Arabica/Robusta beans"),
("090121", "Coffee, roasted, not decaffeinated", "Ground coffee base"),
("090190", "Coffee husks and skins", "By-products"),
("090230", "Black tea, fermented", "Common tea bags"),
("090240", "Other black tea", "Loose leaf"),
("091011", "Ginger, neither crushed nor ground", "Fresh spice"),
("091030", "Turmeric (curcuma)", "Health spice"),
("091091", "Mixtures of spices", "Curry powder"),
("090420", "Pepper, dried/crushed", "Black peppercorns"),
("090520", "Vanilla", "Premium flavoring"),
]
},
"10": {
"title": "Cereals",
"common_mistakes": "In grain vs. milled/flour; durum vs. common wheat.",
"codes": [
("100119", "Durum wheat", "Pasta production"),
("100199", "Other wheat and meslin", "Bread wheat"),
("100590", "Maize (corn), other", "Animal feed staple"),
("100630", "Rice, semi-milled or wholly milled", "White rice"),
("100640", "Broken rice", "Low-grade use"),
("100710", "Grain sorghum", "Feed/alternative"),
("110100", "Wheat flour", "Baking essential"),
]
},
"15": {
"title": "Animal, Vegetable or Microbial Fats and Oils",
"common_mistakes": "Crude vs. refined oil; edible vs. industrial.",
"codes": [
("150710", "Crude soya-bean oil", "Major vegetable oil"),
("150790", "Other soya-bean oil", "Refined for cooking"),
("151110", "Crude palm oil", "Tropical oil staple"),
("151190", "Other palm oil", "Fractionated"),
("151211", "Crude sunflower-seed oil", "Healthy oil"),
("151620", "Vegetable fats and oils", "Margarine base"),
("152000", "Glycerol", "Industrial use"),
]
},
"27": {
"title": "Mineral Fuels, Mineral Oils",
"common_mistakes": "Crude vs. refined; gasoline vs. diesel.",
"codes": [
("270900", "Petroleum oils, crude", "Top global commodity"),
("271012", "Light petroleum distillates", "Gasoline blends"),
("271019", "Medium/heavy petroleum oils", "Diesel/fuel oil"),
("271111", "Natural gas, liquefied", "LNG exports"),
("271121", "Natural gas, gaseous", "Pipeline trade"),
("271311", "Petroleum coke", "Industrial fuel"),
]
},
"30": {
"title": "Pharmaceutical Products",
"common_mistakes": "Medicaments vs. vaccines; packed for retail vs. bulk.",
"codes": [
("300490", "Other medicaments", "Generic drugs, high volume"),
("300215", "Immunological products", "Vaccines/COVID era"),
("300439", "Hormone medicaments", "Insulin/diabetes"),
("300660", "Chemical contraceptive preparations", "Global health"),
("300241", "Vaccines for human medicine", "Essential health"),
("300450", "Vitamins and supplements", "Health products"),
]
},
"39": {
"title": "Plastics and Articles Thereof",
"common_mistakes": "Primary forms vs. articles; polymers vs. waste.",
"codes": [
("390110", "Polyethylene, low density", "Packaging film"),
("390210", "Polypropylene", "Containers/molding"),
("390761", "Polyethylene terephthalate (PET)", "Bottles"),
("391990", "Self-adhesive plates/sheets", "Labels/tapes"),
("392321", "Sacks and bags of polymers", "Plastic bags"),
("392690", "Other plastic articles", "Miscellaneous goods"),
]
},
"71": {
"title": "Natural or Cultured Pearls, Precious Stones",
"common_mistakes": "Unworked vs. worked gems; gold bullion vs. jewelry.",
"codes": [
("710231", "Non-industrial diamonds, unworked", "Gem trade"),
("710812", "Gold, unwrought", "Bullion investment"),
("711319", "Jewellery of precious metal", "Fashion exports"),
("710691", "Silver, unwrought", "Industrial/precious"),
]
},
"72": {
"title": "Iron and Steel",
"common_mistakes": "Flat-rolled vs. bars; alloy vs. non-alloy steel.",
"codes": [
("720810", "Flat-rolled iron/steel, in coils", "Construction material"),
("720917", "Cold-rolled iron/steel sheets", "Automotive use"),
("721049", "Other coated flat-rolled", "Galvanized steel"),
("722540", "Alloy steel flat-rolled", "Tool steel"),
]
},
"84": {
"title": "Nuclear Reactors, Boilers, Machinery and Mechanical Appliances",
"common_mistakes": "Complete machines vs. parts; general vs. specific function.",
"codes": [
("841191", "Parts of turbo-jets", "Aviation engines"),
("847130", "Portable computers (laptops)", "Consumer tech"),
("847330", "Parts of computers", "Motherboards/RAM"),
("848640", "Machines for semiconductor manufacturing", "Chip production"),
("850440", "Static converters", "Power supplies"),
("842952", "Excavators", "Construction machinery"),
("843149", "Parts of machinery", "Heavy equipment"),
("841510", "Air conditioning machines", "HVAC"),
]
},
"85": {
"title": "Electrical Machinery and Equipment",
"common_mistakes": "Smartphones vs. basic phones; processors vs. modules.",
"codes": [
("851712", "Telephones for cellular networks (smartphones)", "Top global import"),
("854231", "Electronic integrated circuits (processors)", "Semiconductors"),
("854140", "Photosensitive semiconductor devices (solar cells)", "Renewable energy"),
("854449", "Other electric conductors", "Cables/wires"),
("850760", "Lithium-ion batteries", "EV/tech demand"),
("852351", "Solid-state drives", "Data storage"),
("853400", "Printed circuits", "Electronics base"),
]
},
"87": {
"title": "Vehicles Other Than Railway or Tramway",
"common_mistakes": "Passenger cars vs. goods vehicles; EV vs. ICE.",
"codes": [
("870323", "Cars with spark-ignition engine 1,500-3,000cc", "Mid-size sedans"),
("870333", "Diesel cars >2,500cc", "SUVs/trucks"),
("870421", "Goods vehicles, diesel", "Light trucks"),
("870899", "Other parts of vehicles", "Auto parts trade"),
("870380", "Electric vehicles", "Growing green trade"),
]
},
"90": {
"title": "Optical, Photographic, Medical Instruments",
"common_mistakes": "Medical vs. non-medical instruments; complete vs. parts.",
"codes": [
("902139", "Artificial joints", "Orthopedic implants"),
("901890", "Other medical instruments", "Surgical tools"),
("903180", "Other measuring instruments", "Testing equipment"),
]
},
"97": {
"title": "Works of Art, Collectors' Pieces and Antiques",
"common_mistakes": "Original vs. reproductions; paintings vs. sculptures.",
"codes": [
("970121", "Paintings, drawings", "Fine art trade"),
("970310", "Original sculptures", "Modern art"),
("970199", "Collages and similar", "Decorative art"),
]
},
"07": {
    "title": "Edible Vegetables and Certain Roots",
    "common_mistakes": "Fresh vs. frozen/chilled; seasonal vs. preserved; roots vs. tubers.",
    "codes": [
        ("070200", "Tomatoes, fresh or chilled", "High-volume salad staple"),
        ("070310", "Onions, fresh or chilled", "Culinary essential, global export"),
        ("070410", "Cauliflower and headed broccoli, fresh", "Vegetable medley trade"),
        ("070511", "Cabbage, fresh", "Basic produce for processing"),
        ("070959", "Other vegetables, fresh (e.g., peppers)", "Mixed fresh veg export"),
        ("071080", "Vegetables, frozen (uncooked)", "Convenience food surge"),
        ("071310", "Peas, frozen, uncooked", "Processed veg leader"),
    ]
},
"17": {
    "title": "Sugars and Sugar Confectionery",
    "common_mistakes": "Raw vs. refined; cane vs. beet; syrups vs. solids.",
    "codes": [
        ("170112", "Raw beet sugar", "Beet sugar alternative to cane"),
        ("170199", "Cane/refined sugar, solid", "Sweetener industry base"),
        ("170230", "Glucose and fructose, solid", "Food/beverage processing"),
        ("170490", "Sugar confectionery (e.g., candies)", "Snack food export"),
        ("180690", "Chocolate preparations", "Confectionery powerhouse"),
    ]
},
"29": {
    "title": "Organic Chemicals",
    "common_mistakes": "Acyclic vs. cyclic; pure vs. derivatives; hazardous vs. non-hazardous.",
    "codes": [
        ("290121", "Ethylene", "Petrochemical building block"),
        ("290211", "Cyclohexane", "Industrial solvent and precursor"),
        ("291411", "Acetone", "Paint/solvent staple"),
        ("291512", "Ethyl acetate", "Adhesives and coatings"),
        ("292419", "Acyclic amides", "Pharma/agro intermediates"),
        ("293299", "Other heterocyclic compounds", "Specialty chemical trade"),
    ]
},
"61": {
    "title": "Articles of Apparel and Clothing Accessories",
    "common_mistakes": "Men's vs. women's; cotton vs. synthetic; outerwear vs. undergarments.",
    "codes": [
        ("610910", "T-shirts and singlets, cotton", "Casual wear global staple"),
        ("611030", "Pullovers, jerseys, cotton", "Knitwear fashion leader"),
        ("610462", "Women's trousers, knitted", "Active/athleisure demand"),
        ("610510", "Men's shirts, knitted", "Everyday apparel"),
        ("611420", "Women's/girls' garments, knitted", "Dresses and suits"),
        ("611595", "Knitted or crocheted socks", "Footwear accessories"),
    ]
},
"73": {
    "title": "Articles of Iron or Steel",
    "common_mistakes": "Tubes vs. pipes; welded vs. seamless; structures vs. fasteners.",
    "codes": [
        ("730531", "Welded pipes/tubes >406mm", "Pipeline/infrastructure trade"),
        ("730431", "Seamless pipes, cold-drawn", "High-pressure applications"),
        ("730830", "Doors, windows, structures", "Construction sector"),
        ("731815", "Screws, bolts, nuts", "Fastener hardware staple"),
        ("732690", "Other articles of iron/steel", "Miscellaneous industrial goods"),
    ]
},
# Add remaining chapters (05-07, 11-26, 28-38, 40-70, 73-83, 86-96) similarly if needed for full 97.
}

# Get styles EARLY
styles = getSampleStyleSheet()

# Create document with extra bottom margin for footer
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=50,
    bottomMargin=80  # Important for footer space
)

# Footer function
def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.drawString(40, 30, "Free resource by Global Link Logistics | Helping exporters navigate global trade | Visit info@globallinklogistics-demo.com for consultations")
    canvas.restoreState()

# Story list
story = []
# ---------- Page 1: Cover + How to Use + Chapter Index ----------
story.append(Paragraph("Global Harmonized System (HS) Code Directory – 2025", styles['Title']))
story.append(Spacer(1, 30))

story.append(Paragraph("A compact, chapter-wise professional reference for international trade", styles['Heading2']))
story.append(Spacer(1, 22))

story.append(Paragraph("Designed for Students, Exporters, Customs Professionals & Analysts", styles['Normal']))
story.append(Spacer(1, 20))

story.append(Paragraph("Prepared by: Ayaan Khan<br/>BCA – UI/UX & Technology Specialization<br/>2025", styles['Italic']))
story.append(Spacer(1, 20))

story.append(Paragraph("""
<b>Note:</b> This directory highlights selected high-trade-volume HS codes for reference (2025 edition). /n
Always verify with official WCO/national sources for binding classifications./nLast updated: December 2025.
""", styles['Normal']))
story.append(Spacer(1, 30))  # Adjusted from 40 to 20 for tighter flow

# How to Use (Expanded)
story.append(Paragraph("<b>How to Use This Directory</b>", styles['Heading3']))
story.append(Spacer(1, 8))
story.append(Paragraph("""
• HS Codes: 6-digit global standard for classifying goods (managed by World Customs Organization)<br/>
• Structure: First 2 digits = Chapter, next 2 = Heading, last 2 = Subheading<br/>
• Why accurate codes matter: Avoid delays, penalties & incorrect duties<br/>
• Refer chapters to classify goods accurately<br/>
• Avoid errors using “Common Mistakes” notes<br/>
• Trade Notes provide real-world examples
""", styles['Normal']))
story.append(Spacer(1, 40))

# Quick HS Code Search Tips
story.append(Paragraph("<b>Quick HS Code Search Tips</b>", styles['Heading3']))
story.append(Spacer(1, 16))

tips_data = [["• Use official tools: WCO HS Database, national tariff schedules"],
             ["• Apply General Rules of Interpretation (GRI) step-by-step"],
             ["• For complex items: Request binding rulings from customs"]]

tips_table = Table(tips_data, colWidths=[500])
tips_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('GRID', (0,0), (-1,-1), 1, colors.lightgrey),  # Box border
    ('BACKGROUND', (0,0), (-1,-1), colors.beige),  # Light box bg
]))
story.append(tips_table)
story.append(Spacer(1, 20))
story.append(PageBreak())

# 2-Column Chapter Index
story.append(Paragraph("<b>Chapter Index</b>", styles['Heading3']))
story.append(Spacer(1, 8))

chapters_list = list(hs_chapters.items())
index_rows = []
for i in range(0, len(chapters_list), 2):
    left = f"Chapter {chapters_list[i][0]} – {chapters_list[i][1]['title']}"
    right = f"Chapter {chapters_list[i+1][0]} – {chapters_list[i+1][1]['title']}" if i + 1 < len(chapters_list) else ""
    index_rows.append([left, right])

index_table = Table(index_rows, colWidths=[260, 260])
index_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('FONTSIZE', (0,0), (-1,-1), 10),
]))
story.append(index_table)
story.append(Spacer(1, 30))

# Top 20 Global Trade Codes Summary
story.append(PageBreak())  # Force new page for summary
story.append(Paragraph("<b>Top 20 High-Volume HS Codes (Global Trade 2025)</b>", styles['Heading2']))
story.append(Spacer(1, 8))
story.append(Paragraph("Quick reference to the world's busiest codes by trade value (est. $10T+). Source: UN Comtrade/WITS.", styles['Normal']))
story.append(Spacer(1, 12))

top20_data = [
    ["HS Code", "Product", "Trade Value (2025 Est.)", "Quick Note"],
    ("851712", "Smartphones", "$500B+", "Consumer electronics leader"),
    ("270900", "Crude petroleum oils", "$800B+", "Energy commodity king"),
    ("870323", "Passenger cars (1.5-3L engine)", "$400B+", "Auto export staple"),
    ("271012", "Gasoline/motor spirit", "$300B+", "Fuel for transport"),
    ("850760", "Lithium-ion batteries", "$200B+", "EV/tech demand surge"),
    ("854231", "Processors/microchips", "$250B+", "Semiconductor boom"),
    ("847130", "Laptops/portable computers", "$150B+", "Remote work essential"),
    ("870899", "Vehicle parts/accessories", "$180B+", "Auto aftermarket"),
    ("390110", "Low-density polyethylene", "$120B+", "Packaging polymer"),
    ("100590", "Maize/corn seed", "$100B+", "Feed/food staple"),
    ("080310", "Bananas/plantains", "$15B", "Top fresh fruit export"),
    ("290121", "Ethylene", "$50B", "Petchem base"),
    ("300490", "Medicaments (mixed)", "$300B+", "Pharma generics"),
    ("720810", "Hot-rolled steel coils", "$150B+", "Construction metal"),
    ("848340", "Gears/transmissions", "$80B", "Machinery parts"),
    ("401110", "Car tires, pneumatic", "$40B", "Vehicle safety"),
    ("841191", "Turbojet parts", "$60B", "Aviation engines"),
    ("852872", "TV receivers (>14\")", "$70B", "Entertainment tech"),
    ("611030", "Knitted pullovers/jerseys", "$20B", "Apparel knitwear"),
]

top20_table = Table(top20_data, colWidths=[60, 150, 80, 150])
top20_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
]))
story.append(top20_table)
story.append(Spacer(1, 20))

# ---------- Chapters (flow naturally, multiple per page) ----------
for chap, data in hs_chapters.items():
    chapter_block = []

    # Chapter title (Modified in loop)
    chapter_style = styles['Heading2']  # Global, but override
    chapter_style.fontSize = 12  # Slightly larger
    chapter_style.fontName = 'Helvetica-Bold'  # Bolder
    chapter_block.append(Paragraph(f"Chapter {chap}: {data['title']}", chapter_style))

    # Table of codes
    table_data = [["HS Code", "Product Description", "Trade Notes"]] + data['codes']
    table = Table(table_data, colWidths=[80, 230, 180])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E4053")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),  # Lighter grid = smaller file
        ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('TOPPADDING', (0,0), (-1,0), 12),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.whitesmoke]),  # Alternating rows optional
    ]))
    chapter_block.append(table)

    # Keep the whole chapter together on one page if possible
    story.append(KeepTogether(chapter_block))
    story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.HexColor("#2E4053"), spaceAfter=10, spaceBefore=5))
    story.append(Spacer(1, 10))  # Reduced from 20 for consistency
    story.append(Spacer(1, 20))  # Space before next chapter




# === FINAL BUILD (ONLY ONCE!) ===
doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)

# Confirmation
print("File exists:", os.path.exists(pdf_filename))
print("Saved at:", pdf_filename)
print("✅ PDF GENERATED SUCCESSFULLY")
print("📄 File location:", pdf_filename)