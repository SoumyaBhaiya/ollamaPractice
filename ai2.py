from ollama import chat
import pdfplumber
import re

# ----- Tool: extract skills -----
def extract_skills(text: str) -> str:
    """
    Simulated tool: returns only the skills found in text as a comma-separated string.
    """
    # Simple regex to pick capitalized words, libraries, or keywords (optional)
    # Here, for demo purposes we just return text; the model will parse it
    return text

# ----- Function to read PDF -----
def read_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# ----- Load resume -----
resume_path = "resume.pdf"
job_description = """ Job description
AI Transformation Engineer (Mon-Fri 8:00am-4:30pm)

On-Site 100% Chandler, AZ

Pay Range:$85,000 - $110,000 Annually

Description

About RK Logistics Group & Project Catalyst

RK Logistics Group is a leading Silicon Valley-based supply chain solutions provider. We are embarking on a massive, industry-defining initiative: Project Catalyst. Inspired by the most aggressive tech-driven acquisition models, we are building a dedicated "RK AI Lab" to acquire traditional, legacy logistics companies and fundamentally transform them using artificial intelligence. We are looking for brilliant, ambitious recent college graduates to join the RK AI Lab. You won't just be maintaining legacy code; you will be part of an elite "integration team" deploying our proprietary AI Transformation Stack to newly acquired companies, driving massive operational overhauls in 90-120 day sprints. If you want to see your code directly impact the physical world—optimizing routes, powering digital twins, and deploying autonomous robotics—this is the place for you.
 

Role Summary

As an AI Transformation Engineer on Project Catalyst, you will bridge the gap between cutting-edge machine learning models and real-world physical operations. You will work alongside senior data scientists and logistics experts to build and deploy intelligent systems across our growing portfolio of acquired companies. This role is highly dynamic, blending software engineering, machine learning deployment, and hands-on operational problem solving.

 

Requirements

Key Responsibilities

Deploy the AI Stack: Assist the integration team in deploying our AI Transformation Stack (intelligent routing, automated dispatch, and predictive intelligence) to newly acquired logistics companies.
Model Training & Fine-Tuning: Help train and refine proprietary machine learning models using vast amounts of real-world supply chain data, creating compounding network effects across our portfolio.
Collaborate on Digital Twins: Work closely with senior engineers to develop Supply
Chain Digital Twins, running simulations to stress-test warehouse layouts and fleet operations before physical execution.
Automate Legacy Processes: Write clean, scalable code to replace manual, paper based workflows with automated, AI-driven solutions (e.g., digital proof of delivery, automated billing).
Rapid Prototyping: Work in 90-120 day transformation sprints, rapidly prototyping and iterating on AI tools that deliver immediate, measurable ROI.
Qualifications & Skills

Education: Recent graduate (Class of 2025 or 2026) with a Bachelor’s or Master’s degree in Computer Science, Artificial Intelligence, Data Science, Operations Research, or a related highly quantitative field.
Programming: Strong proficiency in Python. Familiarity with SQL and data manipulation libraries (Pandas, NumPy).
AI/ML Knowledge: Academic, project, or internship experience with machine learning frameworks (e.g., PyTorch, TensorFlow, Scikit-learn).
Problem Solving: A builder’s mindset. You enjoy tackling complex, messy real-world problems and turning them into elegant, automated solutions.
Communication & Travel: Ability to communicate technical concepts to non-technical operational staff at newly acquired companies. Willingness to travel up to 25% to regional facilities to oversee technology deployment.
Agility: Ability to thrive in a fast-paced, startup-like environment within a larger established company. You are excited by the prospect of transforming traditional industries.
Benefits & Perks

Competitive entry-level base salary with performance-based bonuses tied to successful acquisition transformations.
Comprehensive Health, Dental, and Vision Insurance.
401(k) Plan with Company Match.
Modern, collaborative office environment in Phoenix, AZ.
Accelerated Career Growth: Get in on the ground floor of the RK AI Lab. As the portfolio grows, your leadership opportunities will scale rapidly.
Direct mentorship from senior AI leaders and logistics industry veterans.
RK Qualities & Commitment to Diversity

Adherence to all RK Safety, Quality, ISO, and HR policies and standards.
RK Logistics Group is an equal opportunity employer committed to fostering an inclusive, innovative environment. We encourage candidates from all backgrounds to apply.
RK Logistics Group will consider qualified applicants with a criminal history pursuant to the California Fair Chance Act and applicable local regulations. You do not need to disclose your criminal history or participate in a background check until a conditional job offer is made to you. After making a conditional offer and running a background check, if RK Logistics Group is concerned about a conviction that is directly related to the job, you will be given the chance to explain the circumstances surrounding the conviction, provide mitigating evidence, or challenge the accuracy of the background report. Find out more about the Fair Chance Act by visiting calcivilrights.ca.gov/fair-chance-act.

 RK Logistics Group is an Equal Opportunity Employer committed to fostering a diverse, inclusive, and respectful workplace. We do not discriminate in employment decisions or practices based on race, color, religion, sex (including pregnancy, sexual orientation, and gender identity), national origin, age (40 or older), disability, genetic information, veteran status, or any other legally protected status under applicable federal, state, or local laws. """


resume_text = read_pdf(resume_path)

# ----- Prompt for the model -----
messages = [
    {
        "role": "user",
        "content": (
            "You are a skill extraction assistant.\n"
            "I will provide you a resume and a job description.\n"
            "ONLY return a comma-separated list of skills from the resume that match or are relevant to the job description.\n\n"
            f"Resume:\n{resume_text}\n\n"
            f"Job Description:\n{job_description}"
        )
    }
]

# ----- Call Ollama -----
response = chat(
    model="qwen3",
    messages=messages,
    tools=[extract_skills],  # Model can call it if it wants
    think=False  # Safe on low-powered computers
)

# ----- Print the skills -----
print("Extracted Skills:\n")
print(response.message.content)