.PHONY: all application clean

all: resume_G_Farren.pdf

resume_G_Farren.pdf: industry_resume.tex resume_publications.bib ../publications.bib
	latexmk -pdf -jobname=resume_G_Farren -interaction=nonstopmode -halt-on-error industry_resume.tex

application: resume_G_Farren-application.pdf

resume_G_Farren-application.pdf: industry_resume.tex resume_publications.bib ../publications.bib ../private-contact.tex
	latexmk -pdf -jobname=resume_G_Farren-application -interaction=nonstopmode -halt-on-error industry_resume.tex

clean:
	latexmk -C -jobname=resume_G_Farren industry_resume.tex
	latexmk -C -jobname=industry_resume industry_resume.tex
	latexmk -C -jobname=resume-application industry_resume.tex
	latexmk -C -jobname=resume_G_Farren-application industry_resume.tex
