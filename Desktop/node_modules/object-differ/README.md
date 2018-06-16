# Object-differ
Node module to update deep objects and get notified about changes

## Install
```javascript
$ npm install object-differ
```

## Example
```javascript
var differ = require('object-differ');

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
        'test': 'that isn\'t'
    }
};

// The function will be called whenever a value changes
differ(obj, update, function(key, value, old, path) {
    console.log('Changed', key, 'from', old, 'to', value);
    // OUTPUT: Changed test from object to that isn't
});
```

## Syntax
```javascript
differ(obj, update, callback, notifyObjects, strict)
```
* obj: Target object you want to update (object)
* update: Object containing what you want to replace (object)
* callback: Called whenever a key in obj differs from the matching key in update (function)
* notifyObjects: set to true to get notified about objects (e.g. parents) changing (true, false)
* strict: If update doesn't contain a key, delete it from obj (true, false)
