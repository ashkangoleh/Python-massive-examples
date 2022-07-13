const numbers = [175, 50, 25];



// The reduce() method executes a reducer function for array element.

// The reduce() method returns a single value: the function's accumulated result.

// The reduce() method does not execute the function for empty array elements.

// The reduce() method does not change the original array.

let red = numbers.reduce((total,number)=>{
    return total - number
});

console.log(red);