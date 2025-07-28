//Exercise 1 - Destructuring 
const person = {       //An object 
  name : 'Michael',
  age : 26,
  profession : 'Engineer'
};
const {name, age, profession} = person;   //Destructuring
console.log(`${name} aged ${age}, is an ${profession}.`);   //Using template literal

//Exercise 2 - Adding and removing intergers from an array
let nums = [1, 2, 3, 4, 5];
nums.push(6);           //Added an interger using array.push() 
console.log(nums);
nums.shift();          //Removed the first interger using array.shift()
console.log(nums);