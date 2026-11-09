# One-off content update. Deletes itself after a successful run is not required;
# the caller removes this file.
from pathlib import Path
import shutil

root = Path(r"d:\persnol-website\portfolio-main")
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")

CHECK = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" class="lucide lucide-circle-check w-4 h-4 text-white shrink-0">'
    '<circle cx="12" cy="12" r="10"></circle><path d="m9 12 2 2 4-4"></path></svg>'
)


def icon(cls, inner):
    return (
        '<div class="p-3 rounded-xl border border-white/10 bg-white/5 w-fit text-gray-200">'
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
        'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        'stroke-linejoin="round" class="lucide ' + cls + ' w-6 h-6">' + inner + "</svg></div>"
    )


def item(label):
    return (
        '<li class="flex items-center space-x-2.5">' + CHECK + "<span>" + label + "</span></li>"
    )


def card(svg_cls, svg_inner, title, labels):
    lis = "".join(item(label) for label in labels)
    return (
        '<div class="card-glow p-6 rounded-2xl border border-white/10 bg-[#0c0c0c] space-y-5 transition-all duration-300">'
        + icon(svg_cls, svg_inner)
        + '<h3 class="text-lg font-bold text-white">' + title + "</h3>"
        + '<ul class="space-y-3 text-xs text-gray-300">' + lis + "</ul></div>"
    )


skills = [
    card(
        "lucide-code-xml",
        '<path d="m18 16 4-4-4-4"></path><path d="m6 8-4 4 4 4"></path><path d="m14.5 4-5 16"></path>',
        "Programming",
        ["Python", "JavaScript", "SQL"],
    ),
    card(
        "lucide-monitor",
        '<rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" x2="16" y1="21" y2="21"></line><line x1="12" x2="12" y1="17" y2="21"></line>',
        "Frontend",
        ["HTML", "CSS", "React.js", "Material UI", "Redux Toolkit"],
    ),
    card(
        "lucide-server",
        '<rect width="20" height="8" x="2" y="2" rx="2" ry="2"></rect><rect width="20" height="8" x="2" y="14" rx="2" ry="2"></rect><line x1="6" x2="6.01" y1="6" y2="6"></line><line x1="6" x2="6.01" y1="18" y2="18"></line>',
        "Backend",
        ["FastAPI", "REST API Development"],
    ),
    card(
        "lucide-database",
        '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5V19A9 3 0 0 0 21 19V5"></path><path d="M3 12A9 3 0 0 0 21 12"></path>',
        "Database",
        ["PostgreSQL", "MySQL"],
    ),
    card(
        "lucide-brain",
        '<path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"></path><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"></path><path d="M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4"></path><path d="M17.599 6.5a3 3 0 0 0 .399-1.375"></path><path d="M6.003 5.125A3 3 0 0 0 6.401 6.5"></path><path d="M3.477 10.896a4 4 0 0 1 .585-.396"></path><path d="M19.938 10.5a4 4 0 0 1 .585.396"></path><path d="M6 18a4 4 0 0 1-1.967-.516"></path><path d="M19.967 17.484A4 4 0 0 1 18 18"></path>',
        "AI &amp; Machine Learning",
        ["Machine Learning", "NLP", "Pandas", "NumPy", "Scikit-learn"],
    ),
    card(
        "lucide-sparkles",
        '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"></path><path d="M20 3v4"></path><path d="M22 5h-4"></path><path d="M4 17v2"></path><path d="M5 18H3"></path>',
        "Generative AI",
        ["Gemini API", "LLM Integration", "Prompt Engineering", "RAG"],
    ),
    card(
        "lucide-workflow",
        '<rect width="8" height="8" x="3" y="3" rx="2"></rect><path d="M7 11v4a2 2 0 0 0 2 2h4"></path><rect width="8" height="8" x="13" y="13" rx="2"></rect>',
        "Automation",
        ["n8n", "Workflow Automation", "API Integration", "Webhooks"],
    ),
    card(
        "lucide-wrench",
        '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>',
        "Tools",
        ["Git", "GitHub", "VS Code", "Jupyter Notebook"],
    ),
    card(
        "lucide-braces",
        '<path d="M8 3H7a2 2 0 0 0-2 2v5a2 2 0 0 1-2 2 2 2 0 0 1 2 2v5c0 1.1.9 2 2 2h1"></path><path d="M16 21h1a2 2 0 0 0 2-2v-5c0-1.1.9-2 2-2a2 2 0 0 1-2-2V5a2 2 0 0 0-2-2h-1"></path>',
        "Core Concepts",
        ["OOP", "Data Structures &amp; Algorithms", "Software Testing"],
    ),
]


def replace_once(old, new):
    global html
    count = html.count(old)
    if count != 1:
        raise SystemExit(f"expected 1 occurrence, found {count}: {old[:120]!r}")
    html = html.replace(old, new, 1)


def replace_grid(section_id, new_inner):
    global html
    start = html.find(f'<section id="{section_id}"')
    end = html.find("<section ", start + 1)
    if start < 0 or end < 0:
        raise SystemExit("section not found: " + section_id)
    section = html[start:end]
    marker = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
    grid_at = section.find(marker)
    if grid_at < 0:
        raise SystemExit("grid not found in " + section_id)
    abs_grid = start + grid_at
    # Match the grid div, then replace its children.
    i = abs_grid
    depth = 0
    pos = i
    while pos < len(html):
        next_open = html.find("<div", pos)
        next_close = html.find("</div>", pos)
        if next_close < 0:
            raise SystemExit("unbalanced grid")
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            pos = next_close + len("</div>")
            if depth == 0:
                break
    else:
        raise SystemExit("grid walk failed")
    open_end = html.find(">", abs_grid) + 1
    html = html[:open_end] + new_inner + html[pos - len("</div>") :]


replacements = [
    (
        "Portfolio of Sarath Chandra Patruni — AI/ML Student | Backend Developer | Data & AI Enthusiast. Machine Learning, Generative AI, RAG and scalable backend APIs.",
        "Portfolio of Sarath Chandra Patruni — Computer Science undergraduate specializing in Artificial Intelligence and Machine Learning, software development, backend engineering, and AI-powered applications.",
    ),
    (
        "Building intelligent systems with Machine Learning, Generative AI, RAG and scalable backend APIs.",
        "Building software, backend systems, and AI-powered applications with workflow automation.",
    ),
    (
        "Software Engineering student specializing in AI/ML and Backend Development, currently a Trainee at Technical Hub. Skilled in building end-to-end solutions, from machine-learning models to scalable REST APIs using FastAPI, with hands-on experience in Generative AI, RAG systems, vector databases and data analytics.",
        "Computer Science undergraduate specializing in Artificial Intelligence and Machine Learning, with hands-on experience in software development, backend engineering, AI-powered applications, and workflow automation.",
    ),
    (
        "Analyze data and build ETL pipelines with Pandas &amp; NumPy",
        "Build workflow automations with n8n, APIs, and webhooks",
    ),
    (
        '<div class="text-2xl md:text-3xl font-extrabold text-white">7.9</div><div class="text-xs text-gray-400 font-light leading-tight">CGPA (out of 10)</div>',
        '<div class="text-2xl md:text-3xl font-extrabold text-white">7.7</div><div class="text-xs text-gray-400 font-light leading-tight">B.Tech CSE (AI &amp; ML) CGPA, Aditya College of Engineering and Technology, 2023–2027</div>',
    ),
    (
        '<div class="text-2xl md:text-3xl font-extrabold text-white">89%</div><div class="text-xs text-gray-400 font-light leading-tight">Intermediate Score</div>',
        '<div class="text-2xl md:text-3xl font-extrabold text-white">89%</div><div class="text-xs text-gray-400 font-light leading-tight">Intermediate (MPC), Sri Chaitanya Junior College, 2021–2023</div>',
    ),
    (
        '<div class="text-2xl md:text-3xl font-extrabold text-white">700+</div><div class="text-xs text-gray-400 font-light leading-tight">Competitive Programming Solutions</div>',
        '<div class="text-2xl md:text-3xl font-extrabold text-white">480+</div><div class="text-xs text-gray-400 font-light leading-tight">LeetCode and GeeksforGeeks problems solved</div>',
    ),
    (
        "CodeChef · 400+ Problems",
        "CodeChef",
    ),
    (
        "Data Analytics",
        "Workflow Automation",
    ),
    (
        "Computer Vision",
        "Software Development",
    ),
    (
        "Seeking opportunities in AI/ML, Backend Development and Data Engineering.",
        "Seeking opportunities in software development, AI/ML, and backend engineering.",
    ),
    (
        "A RAG pipeline that converts loan policy documents into dense vector embeddings using Sentence Transformers and stores them in ChromaDB to retrieve relevant information and generate explanations using an LLM.",
        "Processes policy documents with modular ingestion, embeddings, and semantic retrieval. Uses Sentence Transformers and ChromaDB, then an LLM pipeline to explain loan decisions.",
    ),
    (
        "An end-to-end machine-learning system for loan approval prediction using classification models, GridSearchCV for hyperparameter tuning, train-test validation and FastAPI for real-time predictions.",
        "End-to-end Python loan-approval classifier with GridSearchCV tuning. FastAPI and Uvicorn serve validated JSON from modular model loading, preprocessing, and prediction.",
    ),
    (
        'proj-title">AI Resume Analyzer</h3>',
        'proj-title">Resume–Job Description Matching System</h3>',
    ),
    (
        "An AI-powered resume screening system that extracts PDF resume content, uses RAG-based semantic similarity to compare resumes with job descriptions, and generates structured candidate-fit scores and explanations using Gemini and FastAPI.",
        "Python backend that processes PDF resumes and scores candidate-job similarity. FastAPI serves real-time analysis, and Gemini returns match scores, hiring decisions, and feedback.",
    ),
    (
        '<span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Scikit-learn</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">GridSearchCV</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">FastAPI</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Classification</span>',
        '<span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Python</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">GridSearchCV</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">FastAPI</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Uvicorn</span>',
    ),
    (
        '<span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Gemini API</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">RAG</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">FastAPI</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">PDF Processing</span>',
        '<span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Gemini API</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">FastAPI</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">Semantic Matching</span><span class="px-3 py-1 rounded-md border border-white/15 bg-white/5 text-[11px] text-gray-300 font-mono">PDF Processing</span>',
    ),
    (
        '<div class="text-xs font-bold text-white">Email</div><div class="text-[11px] text-gray-400">Connect with me</div>',
        '<div class="text-xs font-bold text-white">Email</div><div class="text-[11px] text-gray-400 break-all">sarathpatruni2@gmail.com</div>',
    ),
    (
        '<div class="text-xs font-bold text-white">LinkedIn</div><div class="text-[11px] text-gray-400">Connect with me</div>',
        '<div class="text-xs font-bold text-white">LinkedIn</div><div class="text-[11px] text-gray-400 break-all">sarath-patruni</div>',
    ),
    (
        '<div class="text-xs font-bold text-white">GitHub</div><div class="text-[11px] text-gray-400">Connect with me</div>',
        '<div class="text-xs font-bold text-white">GitHub</div><div class="text-[11px] text-gray-400 break-all">sarathpatruni</div>',
    ),
    (
        "<span>Available for opportunities</span>",
        '<span>Available for opportunities · <a href="tel:+916281883544" class="hover:text-white transition-colors">+91 62818 83544</a></span>',
    ),
    (
        'about: "Sarath Chandra Patruni is a Software Engineering student specializing in AI/ML and Backend Development, currently a Trainee at Technical Hub. He builds end-to-end solutions — from machine-learning models to scalable REST APIs with FastAPI — with hands-on experience in Generative AI, RAG systems, vector databases and data analytics."',
        'about: "Sarath Chandra Patruni is a Computer Science undergraduate specializing in Artificial Intelligence and Machine Learning, with hands-on experience in software development, backend engineering, AI-powered applications, and workflow automation."',
    ),
    (
        'skills: "Core skills: Python, C++, DSA, OOP · FastAPI, REST APIs, SQL, Uvicorn · ML with Scikit-learn, PyTorch, TensorFlow, GridSearchCV · Generative AI (LLMs, RAG, Sentence Transformers, vector databases) · Pandas, NumPy, ETL · Git, GitHub, Jupyter, Power BI · MySQL, ChromaDB."',
        'skills: "Programming: Python, JavaScript, SQL. Frontend: HTML, CSS, React.js, Material UI, Redux Toolkit. Backend: FastAPI and REST APIs. Databases: PostgreSQL and MySQL. AI and ML: Machine Learning, NLP, Pandas, NumPy, Scikit-learn. Generative AI: Gemini API, LLM integration, prompt engineering, RAG. Automation: n8n, workflow automation, API integration, webhooks. Tools: Git, GitHub, VS Code, Jupyter Notebook. Core concepts: OOP, data structures and algorithms, software testing."',
    ),
    (
        'projects: "Featured projects: 1) Loan Decision Explanation System — a RAG pipeline over loan policy documents using Sentence Transformers, ChromaDB and an LLM. 2) Loan Approval Prediction System — end-to-end ML classification with GridSearchCV and a FastAPI serving layer. 3) AI Resume Analyzer — RAG-based resume vs job-description matching with Gemini and FastAPI."',
        'projects: "Featured projects: 1) Loan Decision Explanation System — policy-document ingestion, embeddings, and semantic retrieval with Sentence Transformers and ChromaDB, connected to an LLM explanation pipeline. 2) Loan Approval Prediction System — an end-to-end Python classifier with GridSearchCV tuning and a FastAPI and Uvicorn API for validated JSON predictions. 3) Resume–Job Description Matching System — a Python backend that processes PDF resumes, scores candidate-job similarity, and uses Gemini for match scores, hiring decisions, and feedback."',
    ),
    (
        'coding: "Competitive programming: 300+ LeetCode problems, 180+ GeeksforGeeks problems and 400+ CodeChef problems — 700+ solutions overall. Profile links are in the About and Contact sections."',
        'coding: "Coding profiles: 300+ problems solved on LeetCode and 180+ problems solved on GeeksforGeeks. LeetCode, GeeksforGeeks, and CodeChef links are in the About and Contact sections."',
    ),
    (
        'contact: "You can email sarathpatruni2@gmail.com or reach out on GitHub (github.com/SarathPatruni). The contact form below also works!"',
        'contact: "Email sarathpatruni2@gmail.com, call +91 62818 83544, or reach out on GitHub (github.com/SarathPatruni) and LinkedIn (sarath-patruni). The contact form below also works."',
    ),
    (
        'experience: "Sarath is currently a Trainee at Technical Hub, working on software engineering and AI/ML projects. Education: B.Tech CGPA 7.9/10, Intermediate 89%."',
        'experience: "Education: B.Tech in Computer Science (Artificial Intelligence and Machine Learning) at Aditya College of Engineering and Technology, 2023–2027, CGPA 7.7/10. Intermediate (MPC) at Sri Chaitanya Junior College, 2021–2023, 89%."',
    ),
]

for old, new in replacements:
    replace_once(old, new)

replace_grid("skills", "".join(skills))

html_path.write_text(html, encoding="utf-8")

src = Path(r"c:\Users\sarat\.cursor\projects\d-persnol-website\attachments\01aae532-2e25-44d3-9656-97f13c3fd503\SDE.pdf")
dest = root / "src" / "resumes" / "Sarath_Res.pdf"
shutil.copyfile(src, dest)
print("updated", html_path)
print("resume bytes", dest.stat().st_size)
