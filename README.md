# fw-assign
These projects are a part of freshworks internship assignment


## JSON-MERGE

Merges a series of files containing JSON array of Objects into a single file containing one JSON object.

### Getting started
Clone the project
```bash 
git clone "https://github.com/alzed/fw-assign.git"
cd fw-assign/json-merge
```
To run the project
```bash
node index.js -f "/Path/to/folder" -i "data" -o "merge" -m 10000

Usage: -i <input folder>

Options:
  --help        Show help                                              [boolean]
  --version     Show version number                                    [boolean]
  -f, --folder  Folder path to read and write files          [string] [required]
  -i, --input   Base name of input files                     [string] [required]
  -o, --output  Base name of the merged file                 [string] [required]
  -m, --max     Maximum size of the merged file              [string] [required]
```

After running this command successfully, you can find a merged json file in the given input folder.
> Technology used: NodeJS, Yargs

> Algorithmic time complexity: O(nk)
>  - n - number of files to be merged
>  - k - distinct root keys of the merged file



## MovieWiki

A web application to enable users to search for any movie and view details
about it.

MovieWiki [Preview](https://rawcdn.githack.com/alzed/fw-assign/addfa360625667ab0fa83317ac1d1460304f3b8f/moviewiki/index.html)
