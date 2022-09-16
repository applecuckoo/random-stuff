// JS variables for Math
// Addition variable is 10 + 10, concatenate strings
var a = 10 + 10;
var addMessage = '10 + 10 = ' + a
// Subtraction variable is 10 - 5
var s = 10 - 5;
var subtractMessage = '10 - 5 = ' + s
// Multiplication variable is 10 * 10
var m = 10 * 10;
var multiplyMessage = '10 * 10 = ' + m
// Division variable is 10 / 5
var d = 10 / 5;
var divideMessage = '10 / 5 = ' + d
// Timing variable
var t = 2000;

function redButtonClear() {
	"use strict";
	// Resets red button to white
	redButton.style.background = "white";
	console.log("Red cleared");
}

function blueButtonClear() {
	"use strict";
	// Resets blue button to white
	blueButton.style.background = "white";
	console.log("Blue cleared");
}

function greenButtonClear() {
	"use strict";
	// Resets green button to white
	greenButton.style.background = "white";
	console.log("Green cleared");
}

function goldButtonClear() {
	"use strict";
	// Resets gold button to white
	goldButton.style.background = "white";
	console.log("Gold cleared");
}

function red() {
    "use strict";
    // Turns the button red
    redButton.style.background = "red";
	console.log("Red pressed, wait for clear");
	setTimeout(redButtonClear, t);
}

function blue() {
    "use strict";
    // Turns the button blue
    blueButton.style.background = "blue";
	console.log("Blue pressed, wait for clear");
	setTimeout(blueButtonClear, t);
}

function green() {
    "use strict";
    // Turns the button green
    greenButton.style.background = "green";
	console.log("Green pressed, wait for clear");
	setTimeout(greenButtonClear, t);
}

function gold() {
    "use strict";
    // Turns the button gold
    goldButton.style.background = "gold";
	console.log("Gold pressed, wait for clear");
	setTimeout(goldButtonClear, t);
}

function add() {
	"use strict";
	// Logs variable to console and alerts variable to user
	alert(addMessage)
	console.log(addMessage)
}

function subtract() {
	"use strict";
	// Logs variable to console and alerts variable to user
	alert(subtractMessage)
	console.log(subtractMessage)
}

function multiply() {
	"use strict";
	// Logs variable to console and alerts variable to user
	alert(multiplyMessage)
	console.log(multiplyMessage)
}

function divide() {
	"use strict";  
	// Logs variable to console and alerts variable to user
	alert(divideMessage)
	console.log(divideMessage)
}