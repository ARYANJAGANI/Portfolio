# Aryan Jagani — Portfolio

A responsive static portfolio for Aryan's work in data engineering, applied AI, and human-centered research. Simplified October 2026 with plain typography, sage, muted blue, and warm sand accents, text-only project cards, and straightforward copy.

Live site: [aryanjagani.github.io/Portfolio](https://aryanjagani.github.io/Portfolio/)

## Preview locally

Run from this folder:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Then open http://localhost:8000. All pages also work as static files, with no framework or build dependency. The site uses system fonts and does not load external font services.

## Editing

- `scripts/build_portfolio.py`: central content, project data, experience, and shared page templates.
- `assets/css/portfolio.css`: design system and responsive layouts.
- `assets/js/portfolio.js`: mobile navigation.
- `assets/images/monogram.svg`: favicon and personal mark.

After changing content, regenerate all six HTML pages:

```sh
python scripts/build_portfolio.py
```

The HTML is pre-rendered so the main content and links work without JavaScript. Projects are split into Data Engineering & Analytics and AI & Machine Learning sections, with three featured projects per track on the homepage. The archive includes all 20 projects and a separate Web & App Explorations section. Section navigation works without JavaScript; the compact mobile menu is progressively enhanced. Existing page URLs are retained: `index.html`, `projects.html`, `experience.html`, `research.html`, `education.html`, and `404.html`.

## Content sources and review notes

The current source of truth is `assets/docs/Aryan_Jagani_Data_Engineer_Resume.pdf`, supplied by Aryan as his latest resume. All resume buttons link to this unchanged PDF. The homepage and supporting pages reflect its data engineering focus, dbt/Snowflake/Airflow stack, production geospatial platform, NSF HDR second-place result, GPA 3.95, and August 2026 graduation.

Current experience dates are September 2025–August 2026 for UMBC iHARP and thesis research, and June–August 2026 for GWU HIVE Lab. The LinkedIn URL and B.E. Computer Science degree wording follow the new resume. Earlier projects and teaching roles remain from the original portfolio where they do not conflict with the latest resume. Existing repository links have not been independently verified. The ELT project uses the demo URL embedded in the supplied resume; no repository URL was invented.

Decorative project illustrations and the illustrated portrait have been removed from the pages. Older assets remain available in the project folder but are not loaded. Existing `robots.txt` restrictions are preserved.

## Publishing

The site is published through GitHub Pages from the `main` branch of `ARYANJAGANI/Portfolio`. If the public domain or repository path changes, update `BASE` in the build script before regenerating.

## Checks

```sh
python scripts/check_portfolio.py
```

Checks local asset and link targets, fragment references, duplicate IDs, main headings, and basic external-link safety. Browser verification covers desktop and mobile layouts, project section navigation, mobile navigation, and research disclosure controls.
