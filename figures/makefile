EPS = $(wildcard *.eps)
SVG = $(wildcard *.svg)
ODG = $(wildcard *.odg)
PY = $(wildcard *.py)
TEX = $(wildcard *.tex)
PDF = $(EPS:.eps=.pdf) $(SVG:.svg=.pdf) $(ODG:.odg=.pdf) $(PY:.py=.pdf) $(TEX:.tex=.pdf)

all: $(PDF)

%.pdf: %.eps
	-epstopdf $<
	pdfcrop $@ $@

%.pdf: %.svg
	inkscape -D -z --file=$< --export-pdf=$@
	pdfcrop $@ $@

%.pdf: %.odg
	libreoffice --headless \
		"-env:UserInstallation=file:///tmp/libreoffice_conversion_${USER}" \
		--convert-to pdf $<
	pdfcrop $@ $@

%.pdf: %.py
	python $<
	pdfcrop $@ $@

%.pdf: %.tex
	latexmk -pdf $<
	pdfcrop $@ $@
	rm -f *.{aux,bbl,blg,fdb_latexmk,fls,log,out,lof,dvi,bcf,run.xml,toc,snm,nav,.gz*}

clean:
	rm -f $(PDF)

.PHONY: all clean
