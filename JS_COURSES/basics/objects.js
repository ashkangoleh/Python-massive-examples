// OBJECTS
const obj = {
    name: "ashkan",
    age: 33,
    "key-three": true,
    //In JavaScript, the this keyword refers to an object. like self in python
    sayMyName:function(){
        console.log(this.name)
    },
    sayRandomName: (name)=>{
        console.log(name)
    }
}
//objectName.propertyName or
//objectName["propertyName"]
console.table(obj)
console.log(obj.name)
console.log(obj['age'])
console.log(obj['key-three'])
obj.sayRandomName("hey")
obj.sayMyName()
let sayName= obj.sayMyName   // with () it will return the function definition
console.log(sayName);

// Object.keys() .values() .entries()

// Object.keys() make an array of keys -> Object.keys(<object name>)
const obj_keys = Object.keys(obj)
console.log(obj_keys);
// Object.values() make an array of values -> Object.values(<object name>)
const obj_values = Object.values(obj)
console.log(obj_values);
// Object.entries() make an array of entries -> Object.entries(<object name>)
const obj_entries = Object.entries(obj)
console.log(obj_entries);


