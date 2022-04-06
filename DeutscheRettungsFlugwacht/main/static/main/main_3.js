// timer and date in nav and header/frontpage
function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);

  var date =
    today.getDate() + "-" + (today.getMonth() + 1) + "-" + today.getFullYear();
  document.getElementById("time").innerHTML =
    date + " | " + h + ":" + m + ":" + s;

  document.getElementById("time_1").innerHTML =
    date + " | " + h + ":" + m + ":" + s;
  setTimeout(startTime, 1000);
}

function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  } // add zero in front of numbers < 10
  return i;
}

// Sonnenaufgang Sonnenuntergang
// Many thanks and best regards for the sunrise and sunset API.
// https://sunrise-sunset.org/api

var request = new XMLHttpRequest();
var d = new Date();
d = d.toString();
d = d.slice(30, 31);
d = parseFloat(d);
console.log(d);

request.open(
  "GET",
  "https://api.sunrise-sunset.org/json?lat=54.216737&lng=9.599856&date=today"
);
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {
    let sunrise = data["results"]["sunrise"];
    let sunset = data["results"]["sunset"];

    console.log(sunset);
    sunrise = parseFloat(sunrise) + d + ":" + sunrise.slice(2, 4);
    console.log(sunrise);
    document.getElementById("sunrise").innerHTML = sunrise;

    sunset = parseFloat(sunset) + (12 + d) + ":" + sunset.slice(2, 4);
    console.log(sunset);
    document.getElementById("sunset").innerHTML = sunset;
  } else {
    console.log("error");
  }
};

request.send();

// Notverfahren
function randomQuestionFlight() {
  let y = Math.floor(Math.random() * questionArrayFlight.length);
  let z = y + 1;
  var x = document.getElementById("flightQues");
  x.innerHTML = "Frage " + z + ": " + '"' + questionArrayFlight[y] + '"';
}
