// Auto-generated. Do not edit!

// (in-package task_2.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let nameAge = require('./nameAge.js');

//-----------------------------------------------------------

class eligibility {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.person = null;
      this.eligi = null;
    }
    else {
      if (initObj.hasOwnProperty('person')) {
        this.person = initObj.person
      }
      else {
        this.person = new nameAge();
      }
      if (initObj.hasOwnProperty('eligi')) {
        this.eligi = initObj.eligi
      }
      else {
        this.eligi = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type eligibility
    // Serialize message field [person]
    bufferOffset = nameAge.serialize(obj.person, buffer, bufferOffset);
    // Serialize message field [eligi]
    bufferOffset = _serializer.string(obj.eligi, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type eligibility
    let len;
    let data = new eligibility(null);
    // Deserialize message field [person]
    data.person = nameAge.deserialize(buffer, bufferOffset);
    // Deserialize message field [eligi]
    data.eligi = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += nameAge.getMessageSize(object.person);
    length += object.eligi.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'task_2/eligibility';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '605e2e8c6dcc5e2732ee00e0daddc6e4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    nameAge person
    string eligi
    ================================================================================
    MSG: task_2/nameAge
    string name
    int64 age
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new eligibility(null);
    if (msg.person !== undefined) {
      resolved.person = nameAge.Resolve(msg.person)
    }
    else {
      resolved.person = new nameAge()
    }

    if (msg.eligi !== undefined) {
      resolved.eligi = msg.eligi;
    }
    else {
      resolved.eligi = ''
    }

    return resolved;
    }
};

module.exports = eligibility;
