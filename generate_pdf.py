"""Generate PDF of the LinkedIn article using reportlab."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import mm

output_path = "/home/user/ai-architecture-for-teams/docs/ai-architecture-linkedin-article.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    leftMargin=25*mm,
    rightMargin=25*mm,
    topMargin=20*mm,
    bottomMargin=20*mm,
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name="AIMarker",
    fontName="Helvetica-Oblique",
    fontSize=9,
    textColor=HexColor("#999999"),
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name="ArticleTitle",
    fontName="Helvetica-Bold",
    fontSize=18,
    textColor=HexColor("#1e1e1e"),
    spaceAfter=14,
    leading=22,
))
styles.add(ParagraphStyle(
    name="SectionHead",
    fontName="Helvetica-Bold",
    fontSize=13,
    textColor=HexColor("#282828"),
    spaceBefore=12,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="SubHead",
    fontName="Helvetica-Bold",
    fontSize=11,
    textColor=HexColor("#333333"),
    spaceBefore=8,
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Body",
    fontName="Helvetica",
    fontSize=10.5,
    textColor=HexColor("#3c3c3c"),
    leading=15,
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Arrow",
    fontName="Helvetica",
    fontSize=10.5,
    textColor=HexColor("#3c3c3c"),
    leading=15,
    spaceAfter=4,
    leftIndent=12,
))
styles.add(ParagraphStyle(
    name="Link",
    fontName="Helvetica",
    fontSize=10.5,
    textColor=HexColor("#0066cc"),
    spaceAfter=6,
))

story = []
sep = HRFlowable(width="30%", thickness=0.5, color=HexColor("#cccccc"), spaceAfter=12, spaceBefore=12)

# --- Content ---
story.append(Paragraph("Drafted by AI \u2014 review before use", styles["AIMarker"]))
story.append(Paragraph("Why I Built an AI Architecture Framework<br/>(And What Most Companies Get Wrong)", styles["ArticleTitle"]))

story.append(Paragraph("Most companies rolling out AI to their teams make the same mistake: they skip the architecture.", styles["Body"]))
story.append(Paragraph('They buy licenses, send a Slack message that says \u201chere\u2019s your login,\u201d and hope for the best. Six months later, nobody trusts the outputs and the whole thing quietly gets shelved.', styles["Body"]))
story.append(Paragraph("Sound familiar? I built something different.", styles["Body"]))

story.append(sep)

story.append(Paragraph("The Problem", styles["SectionHead"]))
story.append(Paragraph("The AI conversation is all about capability. What can it do? How fast? How much money does it save?", styles["Body"]))
story.append(Paragraph("Wrong question.", styles["Body"]))
story.append(Paragraph("The real bottleneck is deployment architecture \u2014 getting AI into a team\u2019s hands in a way that\u2019s compliant, trusted, and doesn\u2019t fall apart when Karen from Finance goes on holiday.", styles["Body"]))
story.append(Paragraph("Three things I kept seeing:", styles["Body"]))
story.append(Paragraph("\u2192 Knowledge trapped in people\u2019s heads (and walking out the door with them)", styles["Arrow"]))
story.append(Paragraph("\u2192 AI adoption that\u2019s basically the Wild West \u2014 no governance, no standards", styles["Arrow"]))
story.append(Paragraph('\u2192 Compliance treated as a \u201cwe\u2019ll figure it out later\u201d problem (spoiler: later is too late)', styles["Arrow"]))

story.append(sep)

story.append(Paragraph("6 Constraints Every Company Should Consider", styles["SectionHead"]))

story.append(Paragraph("1. Compliance before configuration.", styles["SubHead"]))
story.append(Paragraph("You can build an AI workflow in a day. Getting IT to approve it? That\u2019s a season finale cliffhanger. Start approval requests on day one.", styles["Body"]))

story.append(Paragraph("2. Documentation before automation.", styles["SubHead"]))
story.append(Paragraph('You can\u2019t automate what you haven\u2019t documented. And no, that wiki page from 2019 doesn\u2019t count. Use Cognitive Task Analysis \u2014 ask \u201cwhat breaks if you\u2019re not here for two weeks?\u201d and watch the real workflow emerge.', styles["Body"]))

story.append(Paragraph("3. Human-in-the-loop as architecture, not policy.", styles["SubHead"]))
story.append(Paragraph('\u201cAlways review AI output\u201d on a training slide? Cute. Bake it into the system so AI can only produce drafts, never send. That\u2019s architecture.', styles["Body"]))

story.append(Paragraph("4. Tiered rollout, not big bang.", styles["SubHead"]))
story.append(Paragraph("Giving a CLI tool to a team that lives in spreadsheets is like handing someone a Formula 1 car for the school run. Match the tool to the user.", styles["Body"]))

story.append(Paragraph("5. Time budget reality.", styles["SubHead"]))
story.append(Paragraph("Plan for the 4\u20138 hours a week your lead actually has. Not the 20 hours on the fantasy roadmap nobody follows.", styles["Body"]))

story.append(Paragraph("6. Governance from day one.", styles["SubHead"]))
story.append(Paragraph("Your AI context files shape every interaction. If someone silently edits them, your AI\u2019s behavior changes and nobody notices. Branch protection isn\u2019t bureaucracy \u2014 it\u2019s insurance.", styles["Body"]))

story.append(sep)

story.append(Paragraph("Scaling: What Leaders Should Be Asking", styles["SectionHead"]))
story.append(Paragraph("\u2192 Does your AI tool remember context between sessions, or start from zero every time?", styles["Arrow"]))
story.append(Paragraph("\u2192 Are you measuring outcomes (time saved, workflows automated) or just activity (licenses bought, training held)?", styles["Arrow"]))
story.append(Paragraph("\u2192 Can one team\u2019s AI skills be reused by others, or does everyone reinvent the wheel?", styles["Arrow"]))
story.append(Paragraph("\u2192 Is your knowledge capture compounding \u2014 or walking out the door every time someone resigns?", styles["Arrow"]))

story.append(sep)

story.append(Paragraph("Your Move This Week", styles["SectionHead"]))
story.append(Paragraph("1. Pick your 3 most critical workflows. Ask: if the owner left tomorrow, would someone else manage? If not \u2014 start there.", styles["Body"]))
story.append(Paragraph("2. Find out how long compliance approval actually takes. That\u2019s your real timeline.", styles["Body"]))
story.append(Paragraph("3. Stop thinking in tools. Start thinking in architecture.", styles["Body"]))
story.append(Spacer(1, 6))
story.append(Paragraph("AI architecture isn\u2019t a technology problem. It\u2019s a team design problem. The companies that figure this out now will have a compounding advantage over those still debating which chatbot to buy.", styles["Body"]))

story.append(sep)

story.append(Paragraph("The framework is open source:", styles["SubHead"]))
story.append(Paragraph("github.com/sharmingmilan/ai-architecture-for-teams", styles["Link"]))
story.append(Spacer(1, 4))
story.append(Paragraph("Fork it. Break it. Make it yours.", styles["Body"]))

doc.build(story)
print(f"PDF saved to: {output_path}")
