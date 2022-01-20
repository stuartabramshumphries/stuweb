TEX = pandoc
src = template.tex details.yml
FLAGS = --pdf-engine=xelatex

StuartAAHumphries_CV.pdf: $(src)
	$(TEX) $(filter-out $<,$^ ) -o $@ --template=$< $(FLAGS)

.PHONY: clean
clean :
	rm StuartAAHumphries_CV.pdf
