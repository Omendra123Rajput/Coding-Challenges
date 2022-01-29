// Write the function isEmpty(obj) which returns true if the object has no properties, false otherwise.

let schedule = {};

function isEmpty(obj){
    return Object.keys(obj).length === 0 ? true : false

}

alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

alert( isEmpty(schedule) ); // false