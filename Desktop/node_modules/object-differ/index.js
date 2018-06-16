'use strict';

/*function differObject(curr, repl, callbackFunction, notifyObjects, strict, path) {
    if(curr != repl) {
        if(!Array.isArray(path)) path = [];
        var newPath = path.slice();

		for(var key in repl) {
            if(curr[key] != repl[key]) {

                if(typeof repl[key] === 'object') {
                    newPath.push(key);

                    if(typeof curr[key] === 'object') {
                        if(notifyObjects && typeof callbackFunction === 'function') callbackFunction(key, repl[key], curr[key], path);
                        differObject(curr[key], repl[key], callbackFunction, notifyObjects, strict, newPath);
                    } else if(typeof curr[key] !== 'object') {
                        if(notifyObjects && typeof callbackFunction === 'function') callbackFunction(key, repl[key], curr[key], path);
                        differObject((curr[key] = {}), repl[key], callbackFunction, notifyObjects, strict, newPath);
                    }
                } else {
                    if(typeof callbackFunction === 'function') callbackFunction(key, repl[key], curr[key], newPath);
                    curr[key] = repl[key];
                }
            }
		}

        if(strict) {
            for(var key in curr) {
                if(!repl.hasOwnProperty(key)) {
                    if(typeof curr[key] === 'object') {
                        newPath.push(key);

                        if(notifyObjects && typeof callbackFunction === 'function') callbackFunction(key, undefined, curr[key], path);
                        differObject(curr[key], {}, callbackFunction, notifyObjects, strict, newPath);
                    }

                    if(typeof callbackFunction === 'function') callbackFunction(key, undefined, curr[key], newPath);
                    delete curr[key];
                }
            }
        }
    }
}*/

function propagateChange(callback, key, previous, current, path) {
    if(typeof callback === 'function') callback(key, previous, current, path);
}

function differ(previous, replace, callback, objectNotify, strict, path) {
    // Has the object even changed?
    if(previous !== replace) {

        // If path is not an array => make it one
        if(!Array.isArray(path)) path = [];
        let newPath = path.slice();

        for(const key in replace) {
            newPath = path.slice();

            // Has the value changed?
            if(previous[key] !== replace[key]) {

                // The value is an object?! => Do some recursive stuff
                if(typeof replace[key] === 'object') {
                    newPath.push(key);

                    // If the previous value was a primitive type, set it to an empty object
                    if(typeof previous[key] !== 'object') previous[key] = {};

                    if(objectNotify) propagateChange(callback, key, replace[key], previous[key], path);
                    differ(previous[key], replace[key], callback, objectNotify, strict, newPath);

                // It's a primitive value => Go straight ahead
                } else {
                    propagateChange(callback, key, replace[key], previous[key], path);
                    previous[key] = replace[key];
                }
            }
        }

        if(strict) {
            for(const key in previous) {

                // The key is not in the updated object => Propagate changes & delete
                if(!replace.hasOwnProperty(key)) {
                    
                    // The value was an object?! => Do some recursive stuff
                    if(typeof previous[key] === 'object') {
                        newPath.push(key);

                        if(objectNotify) propagateChange(callback, key, undefined, previous[key], path);
                        differ(previous[key], {}, callback, notifyObjects, strict, newPath);

                    // It's a primitive value => Go straight ahead
                    } else {
                        propagateChange(callback, key, undefined, previous[key], path);
                        delete previous[key];
                    }
                }
            }
        }
    }
}

module.exports = differ;
