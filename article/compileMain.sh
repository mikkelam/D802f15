MAIN_LATEX_FILE=main
pdflatex -halt-on-error -draftmode -interaction nonstopmode --shell-escape $MAIN_LATEX_FILE.tex
bibtex main
pdflatex --halt-on-error -draftmode -interaction nonstopmode --shell-escape $MAIN_LATEX_FILE.tex
pdflatex --halt-on-error -interaction nonstopmode --shell-escape $MAIN_LATEX_FILE.tex
