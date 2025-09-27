# Demo-only: simple text parser for a job description
def parse_job_text(text: str):
    title = 'Job'
    required_years = 0
    skills = []
    for l in text.splitlines():
        low = l.lower().strip()
        if low.startswith('title:'):
            title = l.split(':',1)[1].strip()
        if low.startswith('requiredyears:'):
            try:
                required_years = int(l.split(':',1)[1].strip())
            except Exception:
                pass
        if low.startswith('skills:'):
            skills = [s.strip() for s in l.split(':',1)[1].split(',')]
    return {
        'title': title,
        'required_years': required_years,
        'skills': skills,
        'rawText': text
    }
