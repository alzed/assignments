const fs = require('fs');
const path = require('path');
const yargs = require('yargs');

const options = yargs
    .usage("Usage: -i <input folder>")
    .option("f", { alias: "folder", describe: "Folder path to read and write files", type: "string", demandOption: true })
    .option("i", { alias: "input", describe: "Base name of input files", type: "string", demandOption: true })
    .option("o", { alias: "output", describe: "Base name of the merged file", type: "string", demandOption: true })
    .option("m", { alias: "max", describe: "Maximum size of the merged file", type: "string", demandOption: true })
    .argv;

let rawFiles = fs.readdirSync(options.folder);
let merge = path.join(options.folder, `${options.output}.json`);

let keys = [];
let result = [];
let answer = {};

let re = new RegExp(`${options.input}\.+.json`);
let files = rawFiles.filter(rf => re.test(rf));
files.sort((a, b) =>
    a.slice(options.input.length, a.length - 5) - b.slice(options.input.length, b.length - 5)
);

files.forEach((file) => {
    readFile = path.join(options.folder, file);
    let stats = fs.statSync(readFile);
    let fileSizeInBytes = stats["size"];
    if (fileSizeInBytes <= options.max) {
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

result.forEach(res => keys.push(...Object.keys(res)));

let d_keys = new Set(keys);

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

fs.writeFileSync(merge, JSON.stringify(answer));
