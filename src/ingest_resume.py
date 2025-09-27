# Demo-only: simple text parser for a resume snippet
def parse_resume_text(text: str):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    skills = []
    years = 0
    title = 'Candidate'
    for l in lines:
        low = l.lower()
        if low.startswith('skills:'):
            skills = [s.strip() for s in l.split(':',1)[1].split(',')]
        if low.startswith('experienceyears:'):
            try:
                years = int(l.split(':',1)[1].strip())
            except Exception:
                pass
        if low.startswith('title:'):
            title = l.split(':',1)[1].strip()
    return {
        'title': title,
        'skills': skills,
        'experienceYears': years,
        'rawText': text
    }
