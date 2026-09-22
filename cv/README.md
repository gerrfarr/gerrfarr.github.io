# Curriculum vitae

`cv.tex` is the maintained CV source. Publication metadata has exactly one source of truth: [`../publications.bib`](../publications.bib), which also generates the website's publication pages. The CV only stores the keys and ordering of its intentionally shorter selection.

Build and validate the public CV from this directory:

```sh
make
```

The privacy-safe `cv_G_Farren.pdf` is mounted directly into the website at `/cv/cv_G_Farren.pdf`.

`make check` fails if a publication selected in `cv.tex` no longer exists in the shared bibliography.

Build the application version, which additionally includes the home address, phone number, and personal email:

```sh
cp ../private-contact.example.tex ../private-contact.tex  # first time only; then fill it in
make application
```

This creates `cv_G_Farren-application.pdf` locally. Both `private-contact.tex` and the application PDF are ignored by Git and are never included in the website. Both variants come from `cv.tex`; the build name controls whether the private contact block is enabled.

The GitHub Pages build also compiles `cv.tex` before Hugo runs. That makes a deployment fail if the CV cannot be built from the shared bibliography and prevents the checked-in PDF from silently lagging behind the source on the deployed site.

## Scope of the two formats

The website is the comprehensive record for publications, talks, research projects, news, skills, and links. The CV is intentionally selective: it includes first-author and key co-authored publications, selected talks, a shorter employment history, and a fuller awards list. Contact details that are appropriate in the PDF do not need to be duplicated on the public profile.
