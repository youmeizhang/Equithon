var events = require('events');
var eventEmitter = new events.EventEmitter();

var listener1 = function listener1() {
    console.log("sucessfully log in");
}

eventEmitter.on('connection', listener1);

eventEmitter.emit('connection');