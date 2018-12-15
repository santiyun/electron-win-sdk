'use strict'

const addon = require('bindings')('3Ttechapi');

let num ;
num = addon.setRecordingDevice("{0.0.1.00000000}.{1a2419a1-bd2d-4f04-abef-fbc9b95df5f7}");
// num = addon.initialize("a967ac491e3acf92eed5e1b5ba641ab7");
 console.log("test interface return value = ", num );

// let num2 = addon.setchannelprofile(1);
// console.log("setchannelprofile num = ", num2);

// num = addon.enablevideo();
// console.log("enablevideo num = ", num);

// num = addon.setclientrole(1,"liyong");
// console.log("setclientrole num = ", num);

// num = addon.setuplocalvideo(2,0);
// console.log("setuplocalvideo num = ", num);

// num = addon.startpreview();
// console.log("startpreview num = ", num);

// num = addon.joinchannel("chid","59038",0);
// console.log("joidchannel num = ", num);

//num = addon.destroy();
//console.log("destroy num = ", num);

//num = addon.leaveChannel();
//console.log("leaveChannel num = ", num);