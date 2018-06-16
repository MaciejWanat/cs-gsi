var codeStart = process.hrtime();
var differ = require('../index.js');

var obj = {
    'This': 'is',
    'a': {
        'test': 'object',
        'demonstrating': 'the'
    },
    'functionality': ['of', 'object-differ']
};

var update = {
    'a': {
        'test': 'that isn\t'
    }
};

var updateStart = process.hrtime();
differ(obj, update,  null, true, false);

var updateDiff = process.hrtime(updateStart);
var codeDiff = process.hrtime(codeStart);

console.log('Full execution took %dms', codeDiff[0] + (codeDiff[1] / 1000000));
console.log('Bare updating took %dms', updateDiff[0] + (updateDiff[1] / 1000000));
