# portfolio

Personal portfolio website of **Sarath Chandra Patruni** — AI/ML Student | Backend Developer | Data & AI Enthusiast.

## Structure

- `index.html` — the single-page portfolio (hero, about, skills, projects, contact + AI chat widget)
- `projects/` — static, directly accessible project detail routes
- `project-data.js` — shared project detail content
- `project-pages.js` — project card navigation and detail page rendering
- `styles.css` — portfolio styling (dark & light themes, responsive grid)
- `project-details.css` — styling scoped to project detail pages
- `src/` — images (hero portraits, project covers)

## Features

- Dark / light theme toggle with smooth synced transitions
- Local AI chat widget ("Sarath AI") answering questions about skills, projects and coding profiles
- Responsive project grid (1 / 2 / 3 columns)
- Clickable project cards with clean, static detail routes and repository links
- Smooth-scroll navigation, contact form (falls back to email client), resume download
- Coding profile links: LeetCode, GeeksforGeeks, CodeChef, GitHub

## To customize

- Hero photo: `src/1st image-Photoroom.png` (dark theme) and `src/white_theme_home_page.png` (light theme); About photo: `src/2nd_image_about_section.png`.
- Resume is at `src/resumes/Sarath_Res.pdf` (linked from the "Download Resume" button; `Sarath_resume_DA.pdf` is a second, older variant).
- Optionally create a free key at [web3forms.com](https://web3forms.com) and paste it into the `access_key` input in `index.html` to enable direct form submissions (without a key, the form opens the visitor's email client).
- LinkedIn is wired to https://www.linkedin.com/in/sarath-patruni-01-06-jundef (hero icon and contact card).
