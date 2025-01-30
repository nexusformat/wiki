# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

fetch-logo:
#	wget -O ../common/NeXus-logo.png https://raw.githubusercontent.com/nexusformat/definitions/main/manual/source/img/NeXus-logo.png
	wget -O ../common/NeXus_Logo.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo.svg
	wget -O ../common/NeXus_Logo_dark.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark.svg
	wget -O ../common/NeXus_Logo_dark_square.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark_square.svg
	wget -O ../common/NeXus_Logo_square.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_square.svg

html: fetch-logo
	# sphinx-build -b html source build/html
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



