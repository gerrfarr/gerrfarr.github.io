# Industry resume

`industry_resume.tex` is the maintained source for both resume variants.

Build the privacy-safe public resume mounted at `/resume/resume_G_Farren.pdf`:

```sh
make
```

Build the application version with private contact details:

```sh
cp ../private-contact.example.tex ../private-contact.tex  # first time only; then fill it in
make application
```

This creates `resume_G_Farren-application.pdf` locally. Both `private-contact.tex` and the application PDF are ignored by Git and are never included in the website.
