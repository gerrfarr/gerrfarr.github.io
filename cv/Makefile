.PHONY: all application check clean

all: check cv_G_Farren.pdf

check:
	python3 check_publications.py

cv_G_Farren.pdf: cv.tex ../publications.bib
	latexmk -pdf -jobname=cv_G_Farren -interaction=nonstopmode -halt-on-error cv.tex

application: check cv_G_Farren-application.pdf

cv_G_Farren-application.pdf: cv.tex ../publications.bib ../private-contact.tex
	latexmk -pdf -jobname=cv_G_Farren-application -interaction=nonstopmode -halt-on-error cv.tex

clean:
	latexmk -C cv.tex
	latexmk -C -jobname=cv-application cv.tex
	latexmk -C -jobname=cv_G_Farren cv.tex
	latexmk -C -jobname=cv_G_Farren-application cv.tex
