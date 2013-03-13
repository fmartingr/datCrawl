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
