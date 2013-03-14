/*
NodeJS script that wathes for changes on the module and tests folder.

First: install watchr (if you don't have it globally installed):
# npm install wathcr 

Second, execute the script from the root folder (outside utils/ dir)
# node utils/watch.js

Done!

*/


// Requires
var watchr = require('watchr');
var sys = require('sys');
var exec = require('child_process').exec;
var child;

// Start watching files
process.stdout.write('\u001B[2J\u001B[0;0f');
console.log('Unit Testing: Make changes on a file to start tests.');
watchr.watch({
    paths: ['./datCrawl', './test'],
    listeners: {
        change: function(changeType, filePath, fileCurrentStat, filePreviousStat) {
            if (filePath.substr(-3) === ".py") {
                //sys.print('##############################################\n');
                process.stdout.write('\u001B[2J\u001B[0;0f');
                exec("python -m unittest discover",
                    function (error, stdout, stderr) {
                        sys.print(stderr);
                    }
                );
            }
        },
        error: function(err) {
            console.log('an error occured:', err);
        }
    }
});
