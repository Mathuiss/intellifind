# intellifind
Intelligent directory enumerator. Searches startpage, the google proxy for domain and file type.

### Usage

```bash
# Intellifind finds files indexed by google.
# It uses startpage as a proxy

# Find all pdf files on domain.com.
intellifind domain.com

# We can enumerate multiple domains with `,`.
intellifind domain.com,domain2.com,domain3.com

# We can specify the filetype to search for.
intellifind domain.com -f pdf

# We can search for the first 10 pages.
intellifind domain.com -f pdf -c 10

# We can recreate the directory structure. It will make link.txt files.
intellifind domain.com -f pdf -c 10 -o ./data

# We can also download the files directly.
intellidind domain.com -f pdf -c 10 -o ./data --download

```

### Details

```bash
 _       _       _ _ _  __ _           _ 
(_)     | |     | | (_)/ _(_)         | |
 _ _ __ | |_ ___| | |_| |_ _ _ __   __| |
| | '_ \| __/ _ \ | | |  _| | '_ \ / _` |
| | | | | ||  __/ | | | | | | | | | (_| |
|_|_| |_|\__\___|_|_|_|_| |_|_| |_|\__,_|
                                        
                                        

Find files the intelligent way.

Uses startpage as a google proxy to search for files on domains.
Queries like filetype:<type> site:<domain>

usage: intellifind [-h] [-f FILETYPE] [-c COUNT] [-o OUTPUTDIR] [-d] domains

positional arguments:
  domains

options:
  -h, --help            show this help message and exit
  -f FILETYPE, --filetype FILETYPE
  -c COUNT, --count COUNT
  -o OUTPUTDIR, --outputdir OUTPUTDIR
  -d, --download

```

### Install

```bash
# To download
wget https://raw.githubusercontent.com/Mathuiss/intellifind/main/intellifind.py
chmod +x intellifind.py

# To install
sudo cp intellifind.py /usr/bin/intellifind

```