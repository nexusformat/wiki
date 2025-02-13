# # Minimal makefile for Sphinx documentation
# #
#
# # You can set these variables from the command line, and also
# # from the environment for the first two.
# SPHINXOPTS    ?=
# SPHINXBUILD   ?= sphinx-build
# SOURCEDIR     = .
# BUILDDIR      = _build
#
# # Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#
# fetch-logo:
# 	wget -O ./common/NeXus_Logo.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo.svg
# 	wget -O ./common/NeXus_Logo_dark.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark.svg
# 	wget -O ./common/NeXus_Logo_dark_square.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark_square.svg
# 	wget -O ./common/NeXus_Logo_square.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_square.svg
#
# html: fetch-logo
# 	# sphinx-build -b html source build/html
# 	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
#
#
# .PHONY: help Makefile
#
# # Catch-all target: route all unknown targets to Sphinx using the new
# # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# %: Makefile
# 	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)



# File: Makefile

# purpose:
#	build resources in NeXus definitions tree

PYTHON = python3
SPHINX = sphinx-build
BUILD_DIR = build

.PHONY: help install style autoformat test clean prepare html pdf impatient-guide all local nxdl nyaml

help ::
	@echo ""
	@echo "NeXus: Testing the Wiki files and building the documentation:"
	@echo ""

	@echo "make install            Install all requirements to run tests and builds."
	@echo "make style              Check python coding style."
	@echo "make autoformat         Format all files to the coding style conventions."
	@echo "make test               Run documentation tests."
	@echo "make clean              Remove all build files."
	@echo "make prepare            (Re)create all build files."
	@echo "make html               Build HTML version of manual. Requires prepare first."
	@echo "make pdf                Build PDF version of manual. Requires prepare first."
	@echo "make fetch-logo         Copy the official logo files from the manual repository."
	@echo "make all                Builds complete web site for the wiki (in build directory)."
	@echo "make local              (Developer use) Test, prepare and build the HTML wiki."
	@echo ""
	@echo "Note:  All builds of the wiki will occur in the 'build/' directory."
	@echo "   For a complete build, run 'make all' in the root directory."
	@echo "   Developers of the NeXus wiki can use 'make local' to"
	@echo "   confirm the documentation builds."
	@echo ""

install ::
	$(PYTHON) -m pip install -r requirements.txt

style ::
	$(PYTHON) -m black --check dev_tools
	$(PYTHON) -m flake8 dev_tools
	$(PYTHON) -m isort --check dev_tools

autoformat ::
	$(PYTHON) -m black dev_tools
	$(PYTHON) -m isort dev_tools

test ::
	$(PYTHON) -m pytest dev_tools

clean ::
	$(RM) -rf ./wiki/source/$(BUILD_DIR)

prepare ::
	$(PYTHON) -m dev_tools wiki --prepare --build-root $(BUILD_DIR)

# pdf ::
# 	$(SPHINX) -M latexpdf $(BUILD_DIR)/wiki/source/ $(BUILD_DIR)/wiki/build
# 	cp $(BUILD_DIR)/manual/build/latex/nexus.pdf $(BUILD_DIR)/wiki/source/_static/NeXusManual.pdf

html: fetch-logo
	$(SPHINX) -b html -W ./wiki/source/ ./wiki/source/$(BUILD_DIR)/html

# for developer's use on local build host
local ::
	$(MAKE) test
	$(MAKE) prepare
	$(MAKE) html

fetch-logo:
	wget -O ./common/NeXus_Logo.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo.svg
	wget -O ./common/NeXus_Logo_dark.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark.svg
	wget -O ./common/NeXus_Logo_dark_square.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_dark_square.svg
	wget -O ./common/NeXus_Logo_square.svg https://raw.githubusercontent.com/nexusformat/NIAC/master/NeXus_Logo/NeXus_Logo_square.svg

all ::
	$(MAKE) clean
	$(MAKE) prepare
	$(MAKE) pdf
	$(MAKE) html
	@echo "HTML built: `ls -lAFgh $(BUILD_DIR)/wiki/build/html/index.html`"





# NeXus - Neutron and X-ray Common Data Format
#
# Copyright (C) 2008-2024 NeXus International Advisory Committee (NIAC)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org