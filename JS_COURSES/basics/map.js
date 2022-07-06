// Create a Map
const fruits = new Map([
    ["apples", 500],
    ["bananas", 300],
    ["oranges", 200],
]);

console.log(`UNSET: `, fruits);

// You can add elements to a Map with the set() method:
// The set() method can also be used to change existing Map values:
fruits.set("apples", 100);
//The get() method gets the value of a key in a Map:
fruits.get("apples");
console.log(`SET & GET: `, fruits);
//The size property returns the number of elements in a Map:
console.log(`SIZE: `, fruits.size);
//The delete() method removes a Map element:
fruits.delete("apples");
console.log(`DELETED: `, fruits);

//The has() method returns true if a key exists in a Map:
let has = fruits.has("apples");
console.log(has);

// JavaScript Objects vs Maps
// Differences between JavaScript Objects and Maps:
// Object	|Map
// Iterable	|Not directly iterable	|Directly iterable
// Size	|Do not have a size property	|Have a size property
// Key Types	|Keys must be Strings (or Symbols)	|Keys can be any datatype
// Key Order	|Keys are not well ordered	|Keys are ordered by insertion
// Defaults	|Have default keys	|Do not have default keys

//The forEach() method calls a function for each key/value pair in a Map:
let text = "";
fruits.forEach(function (value, key) {
    text += key + " = " + value + "\t";
});
console.log(text);

//The entries() method returns an iterator object with the [key, values] in a Map: looks like .items() in python
let text2 = "";
for (const x of fruits.entries()) {
    text2 += x;
}
console.log(text2);

const _map = new Map([
    ["a", 1],
    ["b", 2],
]);

for (const [key, value] of _map) {
    console.log(`${key}:${value}`);
}
