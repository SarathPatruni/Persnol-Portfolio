window.PORTFOLIO_PROJECTS = {
  "loan-approval-prediction": {
    title: "Loan Approval Prediction System",
    intro: "An end-to-end Python application for automated loan approval prediction using machine-learning classification models.",
    problem: "Loan applications need a consistent way to turn applicant information into an approval prediction rather than requiring each case to be assessed manually.",
    overview: "The project description outlines a modular prediction workflow that accepts applicant data, prepares it for a trained classifier, and returns a structured prediction through a REST API.",
    features: [
      "Classification-based loan approval prediction.",
      "GridSearchCV-based hyperparameter tuning.",
      "FastAPI endpoints served with Uvicorn.",
      "Request validation and structured JSON responses.",
      "Separate model loading, preprocessing, and prediction responsibilities."
    ],
    implementation: "The project description specifies a Python classification model with a modular inference flow: load the model, preprocess the request data, run prediction, and return the result through FastAPI. No matching loan-prediction repository was supplied for source verification; the FastAPI repository is assigned to the Warehouse Management System.",
    technologies: ["Python", "Machine Learning", "Scikit-learn", "FastAPI", "Uvicorn", "REST APIs"],
    workflow: ["Applicant data", "Request validation", "Preprocessing", "Classifier inference", "Structured JSON result"],
    repository: null,
    sourceNote: "Implementation details are based on the project description provided; no repository for this project was supplied."
  },
  "resume-job-matching": {
    title: "Resume–Job Description Matching System",
    intro: "A Python backend that analyzes PDF resumes against job descriptions and uses Gemini to produce candidate-fit results.",
    problem: "Keyword-only screening can miss relevant context in a candidate's experience. This project is intended to compare resume content with a job description and explain the resulting fit.",
    overview: "The repository exposes a FastAPI `/analyze_resume` endpoint that accepts a PDF resume and a form-based job description. Its PDF parser extracts text, and the Gemini prompt requests a match score, shortlist/reject decision, and explanation.",
    features: [
      "PDF resume upload and text extraction with PDFPlumber.",
      "FastAPI `/analyze_resume` endpoint accepting a job description.",
      "Gemini analysis with match-score, decision, and explanation fields.",
      "Sentence Transformers and ChromaDB ingestion/retrieval helpers are present in the repository.",
      "The README describes a React and Vite frontend."
    ],
    implementation: "The active endpoint extracts the uploaded resume text, calls the job-description indexing helper, and passes the resume text and resulting context to Gemini. The repository also contains a separate ChromaDB query helper, but the current endpoint does not call it; the indexing helper does not return the retrieved context. The details here reflect the checked-in code rather than implying a connected semantic-retrieval step.",
    technologies: ["Python", "FastAPI", "Google Gemini API", "PDFPlumber", "Sentence Transformers", "ChromaDB", "React", "Vite"],
    workflow: ["Upload PDF and job description", "Extract resume text", "Index job-description text", "Request Gemini analysis", "Return analysis result"],
    repository: "https://github.com/SarathPatruni/Sarath-smart---AI-Resume-Analyzer"
  },
  "loan-decision-explanation": {
    title: "Loan Decision Explanation System",
    intro: "An AI-powered application that combines a loan prediction model with policy-document retrieval to explain an approval or rejection.",
    problem: "A model's approval decision alone does not explain which lending rules are relevant to an applicant's result.",
    overview: "The FastAPI application loads a serialized loan model, accepts applicant information at `/predict`, and pairs the model decision with a Gemini-generated explanation grounded in retrieved policy text.",
    features: [
      "Loan inference from age, income, credit score, loan amount, and employment.",
      "Policy text is split into chunks and embedded with Sentence Transformers.",
      "ChromaDB stores policy chunks and retrieves relevant passages for a decision.",
      "Gemini generates an explanation using the decision, applicant data, and retrieved policies.",
      "FastAPI returns the approval value and explanation as JSON."
    ],
    implementation: "At startup, the app loads the saved model and serves its static frontend. A `/predict` request is validated as a loan input, converted to a pandas row, and passed to the classifier. The explanation pipeline embeds a query about the result, retrieves policy passages from ChromaDB, and sends those passages with the applicant data and decision to Gemini.",
    technologies: ["Python", "FastAPI", "Scikit-learn", "Pandas", "Sentence Transformers", "ChromaDB", "Google Gemini API", "RAG"],
    workflow: ["Applicant details", "FastAPI `/predict`", "Loan model decision", "Policy retrieval from ChromaDB", "Gemini explanation"],
    repository: "https://github.com/SarathPatruni/Bank-Loan-Analyzer"
  },
  "warehouse-management": {
    title: "Warehouse Management System",
    intro: "A FastAPI backend for managing warehouse products through RESTful CRUD endpoints backed by SQLAlchemy.",
    problem: "Warehouse product records need a straightforward API for creating, viewing, updating, and deleting inventory items.",
    overview: "The application models product records, initializes its database tables and seed data, and exposes product operations through FastAPI routes.",
    features: [
      "Create, retrieve, update, and delete product records.",
      "Collection and item retrieval through `/products` and `/products/{id}`.",
      "SQLAlchemy ORM models and database sessions.",
      "Database sessions provided to request handlers using FastAPI dependency injection.",
      "Automatic table creation and initial product seeding when the table is empty.",
      "CORS configured for the local frontend origin."
    ],
    implementation: "The app creates tables from SQLAlchemy metadata at startup and seeds four sample products when the product table is empty. A generator dependency opens and closes a session for each request. The route handlers perform SQLAlchemy queries and commits for product CRUD operations.",
    technologies: ["Python", "FastAPI", "SQLAlchemy", "Pydantic", "PostgreSQL", "REST APIs", "CORS"],
    workflow: ["Frontend request", "FastAPI route and validation", "Database session dependency", "SQLAlchemy product operation", "JSON response"],
    repository: "https://github.com/SarathPatruni/FastAPI"
  },
  "jarvis-ai-assistant": {
    title: "Jarvis – AI Personal Assistant",
    intro: "A Python personal assistant that combines voice input, Gemini-powered conversations, information lookup, and local desktop actions.",
    problem: "Common desktop tasks and conversational questions often require switching between separate applications and tools.",
    overview: "The repository provides a local command-line assistant and a Streamlit chat interface. Commands can use Gemini for conversational responses, query Wikipedia, or launch supported Windows applications.",
    features: [
      "Local microphone input using SpeechRecognition and Google speech recognition.",
      "Text-to-speech through pyttsx3 in local voice interactions.",
      "Gemini-powered conversations with recent conversation history for context.",
      "Streamlit web UI for text chat, voice actions, and conversation history.",
      "Wikipedia summary lookup; no general web-search integration was found in the inspected source.",
      "Local Windows actions to open Chrome, Calculator, and Notepad, and to launch music search in Chrome.",
      "Conversation history stored in JSON."
    ],
    implementation: "The CLI loop listens for voice commands, dispatches local actions or Gemini requests, and saves each interaction to JSON. The Streamlit app restores saved messages, supports text and voice commands, and passes recent history to the command processor. Microphone, speech output, and desktop automation are local Windows features; the README notes that the deployed Streamlit app is text-chat and Wikipedia focused. gTTS is listed as a dependency, but the inspected speech code uses pyttsx3 and does not call gTTS.",
    technologies: ["Python", "Google Gemini API", "Streamlit", "SpeechRecognition", "pyttsx3", "Wikipedia API", "JSON", "Windows automation"],
    workflow: ["Voice or text input", "Command routing", "Gemini, Wikipedia, or local action", "Text/voice response", "Save conversation to JSON"],
    repository: "https://github.com/SarathPatruni/jarvis-ai-voice-assistant"
  }
};
