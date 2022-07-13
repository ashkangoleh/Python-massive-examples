const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// The slice() method returns selected elements in an array, as a new array.

// The slice() method selects from a given start, up to a (not inclusive) given end.

// The slice() method does not change the original array.

//   ********************* array.slice(start, end)************************* end=(n-1)
const citrus = fruits.slice(1, 3);
const citrus2 = fruits.slice(2);
console.log(citrus);
console.log(citrus2);