/*
 Spacecraft.js simulates a small spacecraft generating telemetry.
*/

//Import mongodb
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

function Spacecraft() {
    this.state = {
        "prop.accx": 1,
        "prop.accy": 0,
        "prop.accz": 0,
        "prop.alt": 0,
        "prop.temp": 0,
        "prop.humid": 0,
        "prop.press": 0,
        "prop.gyrox": 0,
        "prop.gyroy": 0,
        "prop.gyroz": 0,
        "prop.launched": false,
    };
    this.history = {};
    this.listeners = [];
    Object.keys(this.state).forEach(function (k) {
        this.history[k] = [];
    }, this);

    setInterval(function () {
        this.updateState();
        this.generateTelemetry();
    }.bind(this), 25);

    console.log("Example spacecraft launched!");
    console.log("Press Enter to toggle thruster state.");

    process.stdin.on('data', function () {
        this.state['prop.launched'] =
            (this.state['prop.launched'] === false) ? true : false;
        this.state['prop.launched'] = true;
        console.log("Launched " + this.state["prop.launched"]);
        this.generateTelemetry();
    }.bind(this));
};

Spacecraft.prototype.updateState = function () {
    /*
    this.state["prop.accx"] = Math.max(
        0,
        this.state["prop.accx"] -
            (this.state["prop.thrusters"] === "ON" ? 0.5 : 0)
    );
    this.state["pwr.temp"] = this.state["pwr.temp"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());
    if (this.state["prop.thrusters"] === "ON") {
        this.state["pwr.c"] = 8.15;
    } else {
        this.state["pwr.c"] = this.state["pwr.c"] * 0.985;
    }
    this.state["pwr.v"] = 30 + Math.pow(Math.random(), 3);
    */
    //Get the data from the database with stream processing
    MongoClient.connect(url, function (err, db) {
        if (err) throw err;
        var dbo = db.db("telemetry");
        //Find the last record in the database
        dbo.collection("telemetry").find().sort({ _id: -1 }).limit(1).toArray(function (err, result) {
            if (err) throw err;
            console.log(result);
            db.close();
        });
    });

    this.state["prop.accy"] = this.state["prop.accy"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.accz"] = this.state["prop.accz"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.alt"] = this.state["prop.alt"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.temp"] = this.state["prop.temp"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.humid"] = this.state["prop.humid"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.press"] = this.state["prop.press"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.gyrox"] = this.state["prop.gyrox"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.gyroy"] = this.state["prop.gyroy"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.gyroz"] = this.state["prop.gyroz"] * 0.985
        + Math.random() * 0.25 + Math.sin(Date.now());

    this.state["prop.launched"] = false;
};

/**
 * Takes a measurement of spacecraft state, stores in history, and notifies 
 * listeners.
 */
Spacecraft.prototype.generateTelemetry = function () {
    var timestamp = Date.now(), sent = 0;
    Object.keys(this.state).forEach(function (id) {
        var state = { timestamp: timestamp, value: this.state[id], id: id };
        this.notify(state);
        //this.history[id].push(state);
        this.state["comms.sent"] += JSON.stringify(state).length;
    }, this);
};

Spacecraft.prototype.notify = function (point) {
    this.listeners.forEach(function (l) {
        l(point);
    });
};

Spacecraft.prototype.listen = function (listener) {
    this.listeners.push(listener);
    return function () {
        this.listeners = this.listeners.filter(function (l) {
            return l !== listener;
        });
    }.bind(this);
};

module.exports = function () {
    return new Spacecraft()
};