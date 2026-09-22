# Industry Resume Skeleton — Anthropic Research Engineer, Knowledge Team

Working document, not final resume copy. Target length: two pages.

The intended narrative is: **cosmologist and computational researcher who combines scientific leadership with substantial research-engineering and LLM-system development**, demonstrated through CLArXivR and large-scale cosmological data analysis.

---

## Page 1

### GERRIT S. FARREN

Berkeley, CA | [professional email] | [GitHub] | [personal website] | [Google Scholar](https://scholar.google.com/citations?user=JeUYYOUAAAAJ&hl=en)

Do not include a full street address, photograph, date of birth, or the heading “Curriculum Vitae.”

### PROFILE

Two or three lines. Cover only:

- Current professional identity: [cosmologist and computational researcher / cosmologist and research engineer]
- Systems built: [LLM knowledge systems] and [large-scale scientific analysis pipelines]
- Differentiator: [rigorous empirical evaluation] + [reliable implementation] + [research judgment]
- Optional mission connection: [building dependable AI systems that help people reason over complex information]

Preserve the academic identity, but connect it immediately to transferable
research-engineering work. Avoid framing the move as leaving research behind.

### TECHNICAL SKILLS

Keep this compact. Include only technologies that can be discussed comfortably in an interview.

**Languages:** Python | SQL | Bash

**LLM and retrieval:** semantic retrieval | embeddings | reranking | agentic systems | source-grounded evaluation

**Statistical inference:** Bayesian inference | Markov chain Monte Carlo (MCMC) | likelihood modeling | covariance estimation | simulation-based validation

**Scientific computing:** JAX | NumPy/SciPy | numerical integration | scientific emulation

**Distributed systems:** MPI | parallel HDF5 | Slurm

**Engineering:** FastAPI | package and API design | Git | CI/CD | pytest | type checking

Do not use proficiency bars or a long inventory of model and vendor names.

### SELECTED TECHNICAL PROJECTS

#### CLArXivR — Creator & Lead Engineer

[About](https://clarxivr.org/about) | [How it works](https://clarxivr.org/how-it-works) | [GitHub organization, if useful despite private repositories]

Core version — target three bullets:

- **Ownership and product:** Identified a recurring research bottleneck and built and deployed an end-to-end product that ranks each arXiv release against a researcher's own library, reads the strongest matches in full, and explains why they matter; owned product, frontend, backend, evaluation, and deployment for a live beta.
- **Technical capability:** Designed a staged retrieval and LLM-analysis pipeline combining semantic matching, feedback-aware ranking, cross-encoder reranking, and full-paper analysis to surface and explain personally relevant research.
- **Quality and iteration:** Built a fixture-based evaluation suite that measures claim support, coverage, cross-paper connection quality, and evaluator robustness; caught a quality regression during a Gemini migration and used the results to retune prompts before release.

Optional detail if space permits — choose no more than one:

- Agentic research: [tool-using paper chat] that can inspect paper sections, resolve citations, search a user’s library, and retrieve external scientific context. Clearly label as [controlled rollout / active development / deployed], whichever is accurate at application time.
- Infrastructure: independently developed [local arXiv metadata mirror with incremental synchronization] to support reliable retrieval without depending on rate-limited live queries.
- Engineering quality: [automated testing, evaluation isolation, observability, gated deployments, health checks]. Prefer an outcome over test counts unless the count adds real value.

Details to retain for interviews or a portfolio, not necessarily the resume:

- Specific embedding and reranking models
- Individual recommendation algorithms and rank-fusion configuration
- Prompt-registry and judge configuration
- Feedback weights and recency decay
- Synchronization locking and internal deployment topology
- Exact agent tool catalogue

#### DESI × CMB Lensing Analysis — Analysis Lead / Research Software Lead

Target three bullets:

- **Ownership:** Led development and deployment of [measurement and analysis pipeline] for [DESI DR2 CMB-lensing cross-correlation analyses]; clarify [your specific leadership remit and team/collaboration scope].
- **Scale and engineering:** Processed [tens of millions of galaxies across six samples] with [large sky maps / distributed or HPC workflows]; add [data volume, runtime, number of jobs, or another defensible scale measure] if available.
- **Reliability and impact:** Built [validation, systematics-control, reproducibility, and failure-detection mechanisms], enabling [scientific result, collaboration deliverable, or reusable analysis capability].

Possible fourth bullet only if it adds a distinct capability:

- Designed the pipeline for reuse across [galaxy samples, lensing experiments, parameter spaces, or future datasets] and supported [number/type of collaborators or analyses].

Information to supply:

- Approximate team size and number of downstream users
- Your exact ownership versus shared collaboration work
- Compute environment and workflow tools
- Approximate data volume and typical run scale
- One difficult failure mode or systematic you designed around
- Concrete output: publication, data release, collaboration decision, or analysis milestone

#### OPTIONAL THIRD PROJECT — [choose only if it fills a missing capability]

Candidate: [ACT × unWISE pipeline / reusable scientific package / ML emulator / another deployed tool]

Use two bullets maximum:

- What you personally built and why it was technically difficult
- Evidence of reuse, reliability, scientific impact, or adoption

Omit this project if it displaces stronger CLArXivR or DESI evidence.

---

## Page 2

### PROFESSIONAL EXPERIENCE

#### Lawrence Berkeley National Laboratory — Owen Chamberlain Postdoctoral Fellow | Berkeley, CA | Sep 2024–present

Target three or four bullets. Do not repeat project mechanics already covered above.

- Research/engineering remit: [one-line scope]
- Leadership: [co-leading DESI DR2 analysis / Simons Observatory working-group role / other concrete responsibility]
- Collaboration: [team size, disciplines, institutions, code review, coordination, mentoring]
- Broader outcome: [research direction shaped, pipeline adopted, result delivered, or capability established]
- Optional AI-supported work: include only a concrete workflow or system whose effect can be explained; ordinary use of coding assistants does not need a bullet.

#### University of Cambridge — PhD Researcher, Applied Mathematics and Theoretical Physics | Cambridge, UK | Oct 2020–Jul 2024

Target two or three bullets:

- Built [analysis/software/method] for [scientific problem], emphasizing transferable research-engineering work
- Developed [statistical or computational method] and validated it against [data/simulations/baselines]
- Collaborated across [ACT / institutions / research groups] to deliver [selected result]
- Optional communication or mentoring evidence if it adds something not shown at LBNL

Do not summarize the thesis chronologically. Select evidence relevant to Python engineering, empirical ML-style research, evaluation, and collaboration.

#### Earlier Experience — optional compact line

[Affiliate Researcher, LBNL] | [Cambridge teaching roles] | [only include if space remains]

Teaching can demonstrate communication, but should not displace technical evidence.

### SELECTED PUBLICATIONS

Use three concise citations: two published papers and one manuscript in preparation. Maintain the entries in `resume_publications.bib` and the shared `../publications.bib`; do not hand-format citations in the LaTeX source.

- `Farren:DESIDR2CMBLensing` — first-author manuscript in preparation
- `ACT:2023oei` — published first-author unWISE × ACT analysis
- `Sailer:2025lxj` — published joint-first-author optical-depth paper

Then link: **Complete publication list:** [Google Scholar](https://scholar.google.com/citations?user=JeUYYOUAAAAJ&hl=en)

Selection rationale:

- Current first-author work demonstrating measurement ownership and systematic-error control
- Published first-author work built on a substantial analysis pipeline
- Published joint-first-author work demonstrating careful interrogation of assumptions in scientific inference

Do not include a dedicated talks section.

### EDUCATION

**University of Cambridge** — PhD, Applied Mathematics and Theoretical Physics | 2024

Optional short qualifier: [thesis area, only if helpful]

**Haverford College** — BSc, Physics | 2020

No coursework unless it directly establishes an otherwise missing qualification.

### SELECTED RECOGNITION — optional

One compact line or at most two entries:

- Owen Chamberlain Postdoctoral Fellowship
- [one other highly selective award, if useful]

Remove the section entirely if space is needed for engineering evidence.

---

## Resume-wide Editing Rules

### Bullet construction

Each bullet should ideally contain four elements:

1. What you owned
2. What you built or changed
3. The difficult constraint or relevant scale
4. The result or capability created

Preferred pattern:

> [Strong verb] + [system/method] + [technical or organizational constraint] + [result]

Avoid:

- “Worked on,” “helped with,” or “responsible for”
- Unexplained cosmology terminology
- Generic claims such as “used AI,” “worked with big data,” or “built a RAG application”
- Dense inventories of implementation details
- Numbers that cannot be reproduced or defended
- Claims of fine-tuning, reinforcement learning, or online learning unless literally accurate

### Quantification policy

Use numbers when they establish scale and are easy to defend:

- Tens of users
- 700+ processed papers, after confirming the count
- Tens of millions of galaxies
- Six DESI samples
- [team size / runtime / data volume if known]

Use technically specific qualitative language when exact numbers would be fragile:

- “Detected a material loss in coverage and cross-paper connections”
- “Guided prompt retuning during a model migration”
- “Prevented semantic quality regressions”
- “Built reusable validation and systematics-control workflows”

### Detail allocation

- Resume: ownership, architecture category, scale, outcome
- Website/portfolio: diagrams, example outputs, evaluation methodology
- Interview: model choices, ranking algorithms, failure cases, prompt experiments, infrastructure decisions

---

## Open Questions Before Drafting Final Copy

### CLArXivR

- Decide whether to add a restrained scale statement later (for example, beta users or library-paper count) once a stable, easy-to-defend measure is available.
- Decide whether “Creator & Lead Engineer” or “Founder & Lead Engineer” is preferred.
- Confirm the current deployment status of paper chat.
- Identify one concrete user-feedback-driven product change.
- Decide whether any screenshots, sample reports, or architecture material can be made public before applying.

### DESI and large-data analysis

- What exact parts of the DR2 pipeline did you architect and implement?
- What compute tools and environments were used?
- How many people or analyses depend on the pipeline?
- What is the most accessible example of a failure or systematic the pipeline catches?
- Which outcome best demonstrates impact to a non-cosmologist?

### Positioning

- Preferred professional label at the top of the resume
- Whether to include a third technical project
- Which two or three publications best support the engineering narrative
- Whether visa/relocation information belongs in the resume or only the application form
