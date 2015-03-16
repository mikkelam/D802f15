MAIN_LATEX_FILE=main

echo Choose what you want to do
echo 1 - Compile fast
echo 2 - Compile with Table of contents
echo 3 - Compile with references
echo D - Delete files
echo Q - Exit
read -p "Your choice: [1, 2, 3, D, Q]" choice
case $choice in
  3 )
	pdflatex --halt-on-error -interaction nonstopmode $MAIN_LATEX_FILE.tex
	pdflatex --halt-on-error -interaction nonstopmode $MAIN_LATEX_FILE.tex
	bibtex $MAIN_LATEX_FILE
	pdflatex --halt-on-error -interaction nonstopmode $MAIN_LATEX_FILE.tex;&
	
  2 )
	pdflatex --halt-on-error -interaction nonstopmode $MAIN_LATEX_FILE.tex;&
  1 ) 
	pdflatex --halt-on-error -interaction nonstopmode $MAIN_LATEX_FILE.tex;&
  D )
	[ -f *.log ] && rm *.log
	[ -f *.aux ] && rm *.aux
	[ -f *.out ] && rm *.out
	[ -f *.toc ] && rm *.toc
	[ -f *.gz ] && rm *.gz
	[ -f *.bbl ] && rm *.bbl
	[ -f *.blg ] && rm *.blg
	[ -f *.tdo ] && rm *.tdo
	[ -f *.brf ] && rm *.brf
	[ -f *.lot ] && rm *.lot
	[ -f *.dvi ] && rm *.dvi
	[ -f *.lof ] && rm *.lof;;
  * ) read -p "Not valid option";;
esac
