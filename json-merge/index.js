const fs = require('fs');
const path = require('path');
const yargs = require('yargs');

//command line arguments using yargs
const options = yargs
    .usage("Usage: -i <input folder>")
    .option("f", { alias: "folder", describe: "Folder path to read and write files", type: "string", demandOption: true })
    .option("i", { alias: "input", describe: "Base name of input files", type: "string", demandOption: true })
    .option("o", { alias: "output", describe: "Base name of the merged file", type: "string", demandOption: true })
    .option("m", { alias: "max", describe: "Maximum size of the merged file", type: "string", demandOption: true })
    .argv;

//Fetching raw files from the input folder
let rawFiles = fs.readdirSync(options.folder);

//Setting absolute path of the merge file
let merge = path.join(options.folder, `${options.output}.json`);

let keys = [];      //root keys of json files
let result = [];    //json files content
let answer = {};    //merged content of json files

let re = new RegExp(`${options.input}\.+.json`);    //RegEx to filter required json files

//Sorting files based on increasing order of number
let files = rawFiles.filter(rf => re.test(rf));     
files.sort((a, b) =>
    a.slice(options.input.length, a.length - 5) - b.slice(options.input.length, b.length - 5)
);

//Parsing JSON data to result array
files.forEach((file) => {
    readFile = path.join(options.folder, file);
    let stats = fs.statSync(readFile);
    let fileSizeInBytes = stats["size"];
    if (fileSizeInBytes <= options.max) {       //Checking for valid file size
        if (fileSizeInBytes > 0) {
            let read = fs.readFileSync(readFile);   
            result.push(JSON.parse(read));
        }
        else{
            console.log(`File empty, skipping: ${file}`);
        }
    }
    else {
        console.log(`File size exceeded: ${file}`);
    }
});

//Filtering keys of the merged result object data
result.forEach(res => keys.push(...Object.keys(res)));

let d_keys = new Set(keys);     //Fetching distinct keys

//Merging JSON based on unique keys
result.forEach(res => {
    d_keys.forEach(key => {
        if (res[key]) {
            if (answer[key]) {
                answer[key].push(...res[key])
            }
            else {
                answer[key] = res[key]
            }
        }
    })
});

//Writing merged object data output JSON file
fs.writeFileSync(merge, JSON.stringify(answer));
