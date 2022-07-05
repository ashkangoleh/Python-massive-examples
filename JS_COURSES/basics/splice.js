const fruits = ["Banana", "Orange", "Apple", "Mango"];

const _splice = fruits.splice(2, 0, "Lemon", "Kiwi");

const _splice2 = fruits.splice(2, 2);

console.log(_splice);

console.log(_splice2);


// The splice() method adds and/or removes array elements.

// The splice() method overwrites the original array.

// ***************************** array.splice(index, howmany, item1, ....., itemX) *********************