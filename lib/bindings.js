'use strict';
const path = require('path');
const ref = require('@tigerconnect/ref-napi');
const assert = require('assert');

assert(ref.instance);

const bindings = require('node-gyp-build')(path.join(__dirname, '..'));
module.exports = bindings.initializeBindings(ref.instance);
