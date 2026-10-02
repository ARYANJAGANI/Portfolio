"""Build the static portfolio. Run with Python 3; no third-party packages required."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
GITHUB = 'https://github.com/ARYANJAGANI'
LINKEDIN = 'https://www.linkedin.com/in/aryan-jagani'
EMAIL = 'aryanjagani2024@gmail.com'
RESUME = 'assets/docs/Aryan_Jagani_Data_Engineer_Resume.pdf'
BASE = 'https://aryanjagani.github.io/Portfolio/'

def external(url, label, cls=''):
    return f'<a href="{escape(url, quote=True)}" class="{cls}" target="_blank" rel="noopener noreferrer">{label}</a>'

# Content is grounded in the supplied resumes and original portfolio.
PROJECTS = [
    ('Walmart Data Engineering Project','Data engineering','data','bars','An end-to-end TPCH orders pipeline with staging models, fact tables, data marts, reusable macros, and data-quality tests orchestrated through Airflow DAGs.',['dbt','Snowflake','Apache Airflow','SQL'],'https://www.youtube.com/watch?v=vT7Oeu7WqHg&t=2602s'),
    ('Geospatial Research Platform','Production platform · iHARP','data research','climate','A deployed platform for international research teams: hex-level GeoTIFF classification, annotation assignments, QC review queues, and satellite-data export pipelines.',['FastAPI','GCP','SQLite','Render'],'research.html#geospatial'),
    ('Coastal Flood Forecasting Pipeline','NSF HDR Challenge · 2nd place','data ai research','climate','Transformed 70 years of hourly tide-gauge records into features for 14-day forecasting. Achieved ROC-AUC 0.871 and leaderboard F1 0.94 in the NSF HDR Challenge.',['Python','XGBoost','TensorFlow / LSTM'],'NSF-HDR-Challenge-Coastal-Flooding-Forecasting'),
    ('PDF-to-RAG Ingestion Pipeline','Data pipelines & retrieval','data ai','rag','Structure-aware PDF-to-Markdown ingestion, hierarchical chunking, embedding generation, and a persistent vector store with CLI ingestion and retrieval workflows.',['Python','LangChain','ChromaDB','OpenAI'],'PDF-to-RAG'),
    ('Live Market Data Dashboard','Data ingestion & APIs','data web','bars','Ingests live Excel market exports, cleans malformed input, and serves a JSON API and browser dashboard deployed on Render.',['Flask','Pandas','REST API','Render'],'live_ecxel_stock'),
    ('LLMs for Dialogic Reading','Master’s thesis · UMBC','ai research','reading','Reproducible Python/Jupyter evaluations of GPT-4, Gemini, and Llama with tracked prompt versions, model configurations, and versioned results.',['Python','Jupyter','LLM evaluation'],'Masters-Thesis-Umbc'),
    ('Trustworthy AI for Medical Imaging','Explainable AI','ai research','medical','ResNet-based image diagnosis paired with Grad-CAM visual explanations to examine what informs a model’s predictions.',['ResNet','Grad-CAM','Computer vision'],'Toward-Trustworthy-AI-for-Medical-Imaging-ResNet-Based-Diagnosis-with-Grad-CAM-Explanations'),
    ('Botnet Detection','Applied machine learning','ai data','network','Comparing Random Forest, DNN, LSTM, and hybrid models on 5,472 network flow records to identify botnet traffic.',['TensorFlow','Scikit-learn','Network analysis'],'Botnet-detection-From-network-traffic'),
    ('PredictMod','Research tools · GWU HIVE Lab','ai research','rag','A predictive retrieval framework with embeddings and document pipelines to support research and policy modeling workflows.',['Embeddings','Retrieval','Model evaluation'],'PredictMod'),
    ('Business Intelligence Dashboard','Data & analytics','data','bars','A business intelligence project translating data into visual summaries for exploration and decision-making.',['Business intelligence','Visualization'],'BI-Dashboard'),
    ('SQL Analysis Projects','Data & analytics','data','bars','A collection of SQL projects exploring data analysis, querying, and database management.',['SQL','Data analysis'],'sql_projects'),
    ('Real-Time Exercise Tracker','Computer vision · CogniPoseAI','ai research','network','Pose estimation with 33 body keypoints, joint-angle calculations, and repetition counting for live exercise feedback.',['Python','OpenCV','MediaPipe'],'Realtime_fitness_tracker'),
    ('Mental Fitness Tracker','Applied machine learning','ai data','bars','Regression-based analysis of mental fitness patterns across demographic and country-level datasets.',['Python','NumPy','Scikit-learn'],'Mentalfitnesstracker'),
    ('House Price Prediction','Machine learning foundations','ai data','bars','A regression project exploring the relationship between property features and house prices.',['Python','Regression'],'HousePricePrediction'),
    ('Wine Quality Prediction','Machine learning foundations','ai data','bars','Exploring machine learning models to predict wine quality from its measured characteristics.',['Python','Scikit-learn'],'WineQualityPrediction'),
    ('Iris Flower Classification','Machine learning foundations','ai data','network','Classifying iris species from petal and sepal measurements using supervised machine learning.',['Python','Classification'],'IrisFlowerClassification'),
    ('Globe Trotters','Web development','web','climate','A travel-focused frontend website built to explore destinations.',['Frontend','Web design'],'GLOBE-TROTTERS'),
    ('Health Care Chatbot','Application development','web ai','rag','An exploratory healthcare question-and-answer application built with a desktop interface.',['Python','Tkinter'],'questiondiagnosistkinter'),
    ('Weather App','Web development','web','climate','A web project for viewing weather information in a simple interface.',['Frontend','Web development'],'Weather-App'),
    ('Tic Tac Toe','Web development','web','network','An interactive implementation of the classic game, exploring frontend logic and user interaction.',['JavaScript','Game logic'],'TIC-TAC-TOE'),
]

DATA_PROJECTS = {
    'https://www.youtube.com/watch?v=vT7Oeu7WqHg&t=2602s',
    'research.html#geospatial', 'live_ecxel_stock', 'BI-Dashboard', 'sql_projects',
}
WEB_PROJECTS = {'GLOBE-TROTTERS', 'Weather-App', 'TIC-TAC-TOE'}
DEMO_LINKS = {
    'PredictMod': 'https://github.com/ARYANJAGANI/brca-dfs-demo',
}
FEATURED_AI = [
    'NSF-HDR-Challenge-Coastal-Flooding-Forecasting',
    'Masters-Thesis-Umbc', 'PDF-to-RAG',
]

def project_track(project):
    # One primary home per project; technology tags still show cross-disciplinary work.
    repo = project[-1]
    return 'data' if repo in DATA_PROJECTS else 'web' if repo in WEB_PROJECTS else 'ai'

def projects(archive=False):
    tracks = [
        ('data', 'Data Engineering & Analytics', 'Reliable pipelines. Useful insights.',
         'Cloud data platforms, warehouse models, and dashboards that make complex data usable.'),
        ('ai', 'AI & Machine Learning', 'Learning from data. Building with AI.',
         'Forecasting, retrieval systems, and human-centered evaluation—from experiments to applied models.'),
    ]
    if archive:
        tracks.append(('web', 'Web & App Explorations', 'Hands-on foundations.',
                       'Smaller projects exploring frontend development and interactive applications.'))
    output = '<nav class="project-jumps" aria-label="Project sections">'+''.join(
        f'<a href="#{key}-projects">{title}<span aria-hidden="true">↓</span></a>'
        for key,title,_,_ in tracks)+'</nav>'
    index = 0
    for key,title,kicker,description in tracks:
        collection = [project for project in PROJECTS if project_track(project) == key]
        if key == 'ai':
            collection.sort(key=lambda p: FEATURED_AI.index(p[-1]) if p[-1] in FEATURED_AI else len(FEATURED_AI))
        chosen = collection if archive else collection[:3]
        heading, card_heading = ('h2', 'h3') if archive else ('h3', 'h4')
        cards = ''
        for project in chosen:
            index += 1
            name,category,tags_key,kind,desc,tags,repo = project
            url = repo if repo.startswith('https://') or '.html#' in repo else GITHUB+'/'+repo
            demo = f'<p class="project-demo">{external(DEMO_LINKS[name], "View demo ↗", "text-link")}</p>' if name in DEMO_LINKS else ''
            cards += f'''<article class="project-card" data-category="{tags_key}"><div class="project-meta"><span>{category}</span></div><{card_heading} class="project-title">{external(url,escape(name))}</{card_heading}><p>{escape(desc)}</p><div class="project-tags">{''.join('<span>'+escape(tag)+'</span>' for tag in tags)}</div>{demo}</article>'''
        more = '' if archive else f'<a class="text-link collection-more" href="projects.html#{key}-projects">View all {len(collection)} {"data & analytics" if key == "data" else "AI & ML"} projects <span class="arrow">↗</span></a>'
        output += f'''<section class="project-collection track-{key}" id="{key}-projects" aria-labelledby="{key}-projects-title"><div class="collection-heading"><div><{heading} id="{key}-projects-title">{title}</{heading}><p>{description}</p></div><span class="collection-count">{len(chosen):02d} {"projects" if archive else "selected"}</span></div><div class="project-grid">{cards}</div>{more}</section>'''
    return output

ROLES = [
    ('N','Data & Research Engineer · iHARP Fellow','University of Maryland, Baltimore County','Sep 2025–Aug 2026','Architected and shipped a FastAPI geospatial platform for international research teams, integrating GCP object storage, ArcGIS basemaps, and a SQLite workflow layer. Built satellite-data ingestion and export pipelines with annotation tracking and QC review, plus Power BI semantic models and dashboards for the UNDP-aligned Nature Relationship Index.'),
    ('H','Machine Learning & Data Engineer','GWU HIVE Lab (Mazumder Lab) · Remote','Jun–Aug 2026','Built extraction and harmonization pipelines for public multi-omics and PMID-sourced datasets, producing modeling-ready feature tables with automated QC. Containerized analysis workflows with Docker and documented them as BioCompute Objects for FAIR-compliant reproducibility and lab reuse.'),
    ('U','Graduate Researcher · M.S. Thesis','UMBC · Advisor: Prof. Karen Chen','Sep 2025–Aug 2026','Designed reproducible Python/Jupyter pipelines benchmarking GPT-4, Gemini, and Llama. Tracked prompt versions, model configurations, and result sets to support structured experiments and human-centered evaluation of dialogic reading questions.'),
    ('JH','Teaching Assistant','Johns Hopkins Center for Talented Youth','Summer 2026','Supported advanced STEM programming, guided student projects, and provided feedback on machine learning and data science assignments.'),
    ('iC','Programming & STEAM Instructor','iCode Columbia','Summer 2025','Taught Python, Scratch, and interactive coding through project-based learning. Adapted lessons for different skill levels and helped young learners build confidence in computational thinking.'),
    ('B','Machine Learning Intern','Bharat Intern','Aug–Sep 2023','Built regression and classification projects covering house prices, wine quality, and iris species, with an emphasis on preparing data and evaluating models.'),
    ('E','Artificial Intelligence Intern','Edunet Foundation','Jun–Jul 2023','Developed a mental fitness analytics project using Python and scikit-learn. Prepared data, engineered features, and compared regression approaches across country-level datasets.'),
    ('S','Simulation Developer','Shah & Anchor Kutchhi Engineering College','Nov 2021–Mar 2022','Coordinated a team developing a Superposition Theorem simulation for the BEE Virtual Lab. Built and tested interactive learning tools for aspiring engineers.'),
]

def timeline(full=False):
    chosen = ROLES if full else ROLES[:4]
    return '<div class="timeline">'+''.join(f'''<article class="timeline-item"><span class="company-monogram" aria-hidden="true">{monogram}</span><div><div class="timeline-top"><h3>{title}</h3><time>{date}</time></div><p class="organization">{org}</p><p class="role-copy">{desc}</p></div></article>''' for monogram,title,org,date,desc in chosen)+'</div>'

def research(full=False):
    thesis_extra = '''<details class="details"><summary>Read the research approach</summary><p>The thesis uses the CROWD framework: Completion, Recall, Open-ended, Wh-, and Distancing questions. The rubric examines instructional alignment, answerability, text relevance, engagement, age-appropriate vocabulary, and grammar. It compares zero-shot and few-shot prompting, AI-generated and human-authored questions, and the use of LLMs as evaluators.</p></details>''' if full else ''
    paper_extra = '''<details class="details"><summary>Authors & publication details</summary><p>Aryan Jagani, Deepesh Katudia, Miheer Darji, and Vaishali Hirlekar. 2023 International Conference on Self Sustainable Artificial Intelligence Systems (ICSSAS), pp. 188–193. DOI: 10.1109/ICSSAS57918.2023.10331759.</p></details>''' if full else ''
    return f'''<article class="research-card"><span class="research-year">2026</span><div><div class="eyebrow">Master’s thesis · UMBC</div><h3>Evaluating Large Language Models as Generators and Judges of Dialogic Reading Questions for Early Literacy</h3><p>Investigates large language models as both generators and evaluators of dialogic reading questions for early literacy. The research examines question quality and instructional alignment for kindergarten and first-grade learners.</p><p>Aryan Dhiren Jagani · University of Maryland, Baltimore County · ProQuest Dissertations &amp; Theses, 2026 · Publication no. 32792284.</p><p>{external('https://www.proquest.com/docview/3383010044','Read thesis on ProQuest ↗','text-link')}</p>{thesis_extra}</div>{external('https://www.proquest.com/docview/3383010044','<span aria-hidden="true">↗</span><span class="sr-only">Read dialogic reading thesis on ProQuest</span>','research-arrow')}</article>
    <article class="research-card"><span class="research-year">2023</span><div><div class="eyebrow">Conference paper · ICSSAS</div><h3>CogniPoseAI: A Futuristic AI-Enhanced Personal Trainer</h3><p>Using computer vision and pose estimation to analyze exercise posture, count repetitions, and provide real-time feedback.</p>{paper_extra}</div>{external('https://doi.org/10.1109/ICSSAS57918.2023.10331759','<span aria-hidden="true">↗</span><span class="sr-only">Read the CogniPoseAI publication</span>','research-arrow')}</article>'''

def data_research():
    return f'''<article class="research-card" id="geospatial"><span class="research-year">GEO</span><div><div class="eyebrow">Production data platform · iHARP · 2025–2026</div><h3>Satellite data, ready for collaborative research</h3><p>Architected a browser-based platform for hex-level GeoTIFF classification, used by international research teams. A FastAPI backend and SQLite workflow layer connect annotation assignments, QC review queues, and structured exports with GCP object storage and ArcGIS basemaps. Deployed on Render with environment-based configuration.</p><details class="details"><summary>Pipeline & workflow details</summary><p>Ingestion and export pipelines move satellite raster data through classification and review. Assignment tracking and quality-control queues support collaboration, while structured outputs feed downstream research publication.</p></details></div></article><article class="research-card"><span class="research-year">2nd</span><div><div class="eyebrow">National award · NSF HDR Scientific-MOOD FAIR Challenge · March 2026</div><h3>Coastal flood forecasting, from raw records to predictions</h3><p>Placed second nationally in the Year 2 Coastal Flooding Prediction track. Parsed 70 years of hourly tide-gauge records from MATLAB datenum format, aggregated to daily grain, and engineered rolling windows for 14-day forecasts. ROC-AUC: 0.871. Leaderboard F1: 0.94.</p></div>{external('https://www.nsfhdr.org/html/mlchallenge-y2/winners.html','<span aria-hidden="true">↗</span><span class="sr-only">View NSF HDR Challenge winners</span>','research-arrow')}</article>'''

def eyebrow(number, text):
    return ''

def header(home=False, current=''):
    prefix = '' if home else 'index.html'
    links = [('Work', 'work'),('About','about'),('Experience','experience'),('Research','research')]
    nav = ''.join(f'<a href="{prefix}#{key}"'+(' aria-current="page"' if current == key else '')+f'>{label}</a>' for label,key in links)
    return f'''<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="wrap nav-bar"><a class="brand" href="index.html" aria-label="Aryan Jagani home">Aryan Jagani</a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation">Menu +</button><nav class="nav-links" id="site-navigation" aria-label="Main navigation">{nav}<a href="{prefix}#contact">Let’s talk <span class="arrow">↗</span></a>{external(RESUME,'Résumé <span class="arrow" aria-hidden="true">↓</span>','nav-resume')}</nav></div></header>'''

def footer():
    return f'''<section class="contact-section" id="contact" aria-labelledby="contact-title"><div class="wrap contact-inner"><div><h2 id="contact-title">Let’s connect</h2><p>Feel free to reach out about a role, a project, or a research collaboration.</p></div><div class="contact-actions"><a href="mailto:{EMAIL}">{EMAIL} <span class="arrow">↗</span></a><div class="contact-socials">{external(GITHUB,'GitHub ↗')}{external(LINKEDIN,'LinkedIn ↗')}{external(RESUME,'Résumé ↓')}</div></div></div></section><footer class="wrap site-footer"><span>© 2026 Aryan Jagani</span><div class="footer-right"><a href="education.html">Education ↗</a><a href="#top">Back to top ↑</a></div></footer>'''

def page(filename,title,description,body,current='',home=False):
    schema = {'@context':'https://schema.org','@type':'Person','name':'Aryan Jagani','url':BASE,'sameAs':[GITHUB,LINKEDIN],'alumniOf':[{'@type':'CollegeOrUniversity','name':'University of Maryland, Baltimore County'},{'@type':'CollegeOrUniversity','name':'Shah & Anchor Kutchhi Engineering College'}]}
    html = f'''<!DOCTYPE html>
<html lang="en" id="top"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | Aryan Jagani</title><meta name="description" content="{escape(description,quote=True)}"><meta name="theme-color" content="#f8f7f3"><meta property="og:title" content="{title} | Aryan Jagani"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE + ('' if home else filename)}"><link rel="icon" href="assets/images/monogram.svg" type="image/svg+xml"><link rel="canonical" href="{BASE + ('' if home else filename)}"><link rel="stylesheet" href="assets/css/portfolio.css"><script src="assets/js/portfolio.js" defer></script>{'<script type="application/ld+json">'+json.dumps(schema)+'</script>' if home else ''}</head><body>{header(home,current)}<main id="main">{body}</main>{footer()}</body></html>'''
    (ROOT/filename).write_text(html,encoding='utf-8')

def build():
    hero = f'''<div class="wrap"><section class="hero" aria-labelledby="hero-title"><p class="hero-role">Data engineer · Baltimore, MD</p><h1 id="hero-title">Hi, I’m Aryan.</h1><p class="hero-copy">I build data pipelines, cloud platforms, and machine learning tools. I recently completed my M.S. in Information Systems at UMBC, where I worked on geospatial data systems and AI research.</p><div class="button-row"><a class="button button-primary" href="#work">View my projects</a>{external(RESUME,'View résumé','button button-secondary')}<a class="text-link" href="mailto:{EMAIL}">Get in touch</a></div><p class="hero-note">Open to data engineering opportunities and relocation.</p></section>
    <section class="section" id="about" aria-labelledby="about-title"><h2 class="about-heading" id="about-title">About me</h2><div class="about-layout"><div class="about-body"><p>I’m Aryan, a data engineer based in Baltimore, with an M.S. in Information Systems from <strong>the University of Maryland, Baltimore County</strong> (August 2026, GPA 3.95) and a B.E. in Computer Science.</p><p>My work spans ELT pipelines, warehouse modeling, and cloud data platforms. I’ve shipped a geospatial platform used by international research teams, built reproducible biomedical data workflows, and placed <strong>second nationally in the NSF HDR coastal flooding challenge.</strong></p><p>I like working through the practical parts of a project: cleaning the data, building the pipeline, and checking whether the results are useful. I’ve also taught programming at iCode and Johns Hopkins CTY.</p></div><img class="about-portrait" src="assets/images/aryan-portrait.jpeg" alt="Aryan Jagani wearing a navy suit outdoors" width="768" height="1024" loading="lazy" decoding="async"></div><div class="expertise-grid"><div class="expertise"><b>Modern data stack</b><p>dbt · Snowflake · Airflow<br>SQL · Python · Spark<br>Data modeling · Data quality</p></div><div class="expertise"><b>Cloud & platforms</b><p>GCP · Docker · Git · CI/CD<br>FastAPI · Flask · REST APIs<br>PostgreSQL · MySQL · SQLite</p></div><div class="expertise"><b>Analytics & research</b><p>Power BI · DAX · Plotly · R<br>Pandas · XGBoost · LLMs<br>FAIR data · BioCompute Objects</p></div></div><div class="education-strip"><div><span class="eyebrow">2024–2026 · Graduate study</span><h3>M.S. Information Systems</h3><p>University of Maryland, Baltimore County · August 2026 · GPA 3.95</p></div><div><span class="eyebrow">2020–2024 · Undergraduate study</span><h3>B.E. Computer Science</h3><p>Shah & Anchor Kutchhi Engineering College · Mumbai, India · May 2024</p></div></div></section>
    <section class="section" id="work" aria-labelledby="work-title">{eyebrow('01','Selected work')}<div class="section-heading"><h2 id="work-title">Selected projects</h2><a class="text-link" href="projects.html">Explore all projects <span class="arrow">↗</span></a></div>{projects()}</section>
    <section class="section" id="experience" aria-labelledby="experience-title"><div class="experience-layout"><div class="experience-intro">{eyebrow('03','The journey so far')}<h2 id="experience-title">Experience</h2><p>Building production platforms, reproducible pipelines, and research tools has shaped how I approach data engineering.</p><a href="experience.html" class="text-link">View full experience <span class="arrow">↗</span></a></div>{timeline()}</div></section>
    <section class="section" id="research" aria-labelledby="research-title">{eyebrow('04','Research & writing')}<div class="section-heading"><h2 id="research-title">Research</h2><a href="research.html" class="text-link">More about my research <span class="arrow">↗</span></a></div>{research()}</section></div>'''
    page('index.html','Data Engineering & Applied AI','Aryan Jagani — data engineer and UMBC graduate building ELT pipelines, cloud data platforms, and warehouse models with dbt, Snowflake, Airflow, SQL, and Python.',hero,home=True)
    page('projects.html','Projects','Explore Aryan Jagani’s projects in ELT pipelines, cloud data platforms, climate forecasting, retrieval systems, and analytics.',f'<div class="wrap"><header class="page-hero">{eyebrow("Portfolio","Project archive")}<h1>Projects</h1><p>Projects in data engineering, analytics, and machine learning, along with a few earlier web applications.</p></header><section class="page-body" aria-label="Project collection">{projects(True)}</section></div>',current='work')
    page('experience.html','Experience','Research and teaching experience at UMBC iHARP, Johns Hopkins CTY, George Washington University HIVE Lab, and iCode Columbia.',f'<div class="wrap"><header class="page-hero">{eyebrow("Background","Experience")}<h1>Experience</h1><p>From research labs to classrooms, I build systems, explore questions, and help others find their footing in technology.</p></header><section class="page-body" aria-label="Work experience">{timeline(True)}</section></div>',current='experience')
    page('research.html','Research','Aryan Jagani’s research on LLM-generated questions for dialogic reading and CogniPoseAI, a computer vision exercise trainer.',f'<div class="wrap"><header class="page-hero">{eyebrow("Research","Questions & discoveries")}<h1>Research</h1><p>My research interests span large language models, human-centered evaluation, computer vision, and the relationship between data and our environment.</p></header><section class="page-body" aria-label="Research publications and thesis">{research(True)}{data_research()}<article class="research-card"><span class="research-year">NRI</span><div><div class="eyebrow">Interdisciplinary research · iHARP</div><h3>Understanding our relationship with nature</h3><p>Built Power BI semantic models and dashboards for the UNDP-aligned Nature Relationship Index, including global choropleths, country profiles, and cross-version indicator comparisons.</p></div>{external("https://hdr.undp.org/nature-relationship-index",'<span aria-hidden="true">↗</span><span class="sr-only">Explore the UNDP Nature Relationship Index</span>',"research-arrow")}</article></section></div>',current='research')
    page('education.html','Education','Aryan Jagani’s M.S. in Information Systems from UMBC, completed August 2026, and B.E. in Computer Science.',f'''<div class="wrap"><header class="page-hero">{eyebrow('Background','Education')}<h1>Education</h1><p>Computer science foundations, graduate research, and a continuing interest in how technology can help people.</p></header><section class="page-body" aria-label="Education"><article class="education-card"><span class="year">2024–2026</span><div><h2>M.S. Information Systems</h2><h3>University of Maryland, Baltimore County</h3><p>Graduated August 2026 · GPA 3.95. Thesis: Evaluating LLMs for Dialogic Reading. Research focused on educational question generation, instruction-focused rubrics, prompting strategies, and human-centered evaluation.</p></div></article><article class="education-card"><span class="year">2020–2024</span><div><h2>B.E. Computer Science</h2><h3>Shah & Anchor Kutchhi Engineering College · Mumbai, India</h3><p>Foundations in computer architecture, artificial intelligence, learning algorithms, and computational theory. Developed an interactive virtual lab simulation and co-authored the CogniPoseAI conference paper.</p></div></article><article class="education-card"><span class="year">2018–2020</span><div><h2>Higher Secondary Education</h2><h3>Mithibai College</h3></div></article></section></div>''',current='about')
    page('404.html','Page Not Found','This page could not be found. Explore Aryan Jagani’s projects and research.', '<div class="wrap"><section class="not-found"><div class="eyebrow">404 / A small detour</div><h1>This path is still<br><em class="serif">unexplored.</em></h1><p>The page you’re looking for may have moved. There’s plenty to explore back at the portfolio.</p><a class="button button-primary" href="index.html">Back to the portfolio ↗</a></section></div>')
    print('Built index, projects, experience, research, education, and 404 pages.')

if __name__ == '__main__':
    build()
