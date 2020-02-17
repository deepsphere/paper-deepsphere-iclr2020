TEX = $(wildcard *.tex)
PDF = $(TEX:.tex=.pdf)
BBL = $(TEX:.tex=.bbl)
BIB = $(wildcard *.bib)
BST = $(wildcard *.bst)
STY = $(wildcard *.sty)

all: $(PDF)

figures:
	$(MAKE) -C figures

%.pdf: %.tex $(BIB) $(STY) $(BST) figures
	latexmk -pdf $<

%.bbl: %.tex $(BIB) $(STY) $(BST) figures
	latexmk -pdf $<

clean:
	#git clean -Xdf
	rm -f *.{aux,bbl,blg,fdb_latexmk,fls,log,out,lof,dvi}
	rm -f *.{bcf,run.xml}
	rm -f *.{toc,snm,nav}
	rm -f *.cls
	rm -f *.gz*
	rm -f *.pdfpc

cleanall: clean
	$(MAKE) clean -C figures
	rm -f $(PDF)
	rm -f arxiv.zip

arxiv.zip: $(TEX) $(BBL) $(STY)
	apack arxiv.zip $(TEX) $(BBL) $(STY) figures/*.{pdf,png,jpg}

.PHONY: all figures clean cleanall
