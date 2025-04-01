README
======

This is the source for https://www.nexusformat.org (when hosted as Github Pages).

To build the wiki with a conda environment, execute the following commands:

Clone the repository:
```bash
git clone https://github.com/nexusformat/wiki.git
```
Create the conda environment and activate it:
```bash
conda create -n nexuswiki python=3.12
conda activate nexuswiki
```
Install the required packages:
```bash
make install
```
Build the wiki:
```bash
make html
