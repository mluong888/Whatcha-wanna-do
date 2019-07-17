function myFunction(){
    // var select = document.getElementsByClassName("cbox").getElementsByClassName("cboxtext")[0];
    // alert(select);
    var table = document.getElementById("checklist");
    if (table!=null){
        console.log(table.rows.length);
        console.log(table.rows[0].cells.length);
        for (var i = 0; i<table.rows.length; i++){
            for (var j = 0; j<table.rows[i].cells.length; j++){
                table.rows[i].cells[j].onclick = function(){
                    alert(this.innerHTML.substring(133,this.innerHTML.length));
                    // console.log(this.innerHTML.substring(140,this.innerHTML.length));
                    var text = this.innerHTML.substring(140,this.innerHTML.length);
                    var textlist = text.split("<br>");
                    var title = textlist[0].trim();
                    var date = textlist[1].trim();
                    var start = date.substring(11,19);
                    var end = date.substring(20,date.length);
                    console.log(title);
                    createEvent(start,end, title);
                    // console.log(date);
                    // console.log(start);
                    // console.log(end);
                    // for (var k=0; k <text.length; k++){
                    //     if counter == 0:
                    //         title.concat(text.charAt(k));
                    //
                    // }
                }
            }
        }
    }
    // var text = document.getElementsByClassName("cboxtext")[0].innerHTML;
    // console.log(text)
    // alert(text);
}


//from website!!!
//============================================
const containerHeight = 720;
const containerWidth = 600;
const minutesinDay = 60 * 12;
let collisions = [];
let width = [];
let leftOffSet = [];

// append one event to calendar
var createEvent = (start, end, title) => {

  let node = document.createElement("DIV");
  node.className = "event";
  node.innerHTML =
  "<span class='title'>" + title + "</span>"
  console.log(title);
  // " \
  // <br><span class='location'> Sample Location </span>";

  // Customized CSS to position each event
  // node.style.width = (containerWidth/units) + "px";
  // node.style.height = height + "px";
  // node.style.top = top + "px";
  // node.style.left = 100 + left + "px";

  document.getElementById("events").appendChild(node);
  // node.style.position = "relative";
  node.style.position = "absolute";

  // timeslot(start,end);
  var slotlst = timeslot(start, end);
  console.log(slotlst[0])
  var pushdown = (slotlst[0] - 480)/60 * 46 + 975
  // var pushdown = slotlst[0]/30 * 25 + 975 - 480;
  node.style.top = pushdown + "px";
  node.style.height = slotlst[1]/30 * 23;

  //every half hour is 26px
  // node.style.top = "200px";

}

function timeslot (start, end) {
    //return diff of start -> end in minutes
    var init = start.substring(0,2);
    var initdeci = start.substring(3,5);
    var final = end.substring(0,2);
    var finaldeci = end.substring(3,5);

    var initconv = parseInt(init) * 60 + parseFloat(initdeci);
    var finalconv = parseInt(final) * 60 + parseFloat(finaldeci);
    var diff = finalconv - initconv;
    console.log(diff);
    return [initconv, diff];

}
// timeslot("11:30", "19:15");

function getCollisions (events) {

  //resets storage
  collisions = [];

  for (var i = 0; i < 24; i ++) {
    var time = [];
    for (var j = 0; j < events.length; j++) {
      time.push(0);
    }
    collisions.push(time);
  }

  events.forEach((event, id) => {
    let end = event.end;
    let start = event.start;
    let order = 1;

    while (start < end) {
      timeIndex = Math.floor(start/30);

      while (order < events.length) {
        if (collisions[timeIndex].indexOf(order) === -1) {
          break;
        }
        order ++;
      }

      collisions[timeIndex][id] = order;
      start = start + 30;
    }

    collisions[Math.floor((end-1)/30)][id] = order;
  });
};

/*
find width and horizontal position

width - number of units to divide container width by
horizontal position - pixel offset from left
*/
function getAttributes (events) {

  //resets storage
  width = [];
  leftOffSet = [];

  for (var i = 0; i < events.length; i++) {
    width.push(0);
    leftOffSet.push(0);
  }

  collisions.forEach((period) => {

    // number of events in that period
    let count = period.reduce((a,b) => {
      return b ? a + 1 : a;
    })

    if (count > 1) {
      period.forEach((event, id) => {
        // max number of events it is sharing a time period with determines width
        if (period[id]) {
          if (count > width[id]) {
            width[id] = count;
          }
        }

        if (period[id] && !leftOffSet[id]) {
          leftOffSet[id] = period[id];
        }
      })
    }
  });
};
var layOutDay = (events) => {

// clear any existing nodes
var myNode = document.getElementById("events");
// myNode.innerHTML = '';

  // getCollisions(events);
  // getAttributes(events);

  events.forEach((event, id) => {
    // let height = (event.end - event.start) / minutesinDay * containerHeight;
    // let top = event.start / minutesinDay * containerHeight;
    // let end = event.end;
    // let start = event.start;
    // let units = width[id];
    // if (!units) {units = 1};
    // let left = (containerWidth / width[id]) * (leftOffSet[id] - 1) + 200;
    // if (!left || left < 0) {left = 10};
    createEvent(event.start, event.end, "test");
  });
}
const events = [{start: "10:00", end: "11:00"}, {start: "11:00", end: "12:00"}, {start: "12:00", end: "13:00"}, {start: "13:00", end: "14:00"} ];

layOutDay(events);
