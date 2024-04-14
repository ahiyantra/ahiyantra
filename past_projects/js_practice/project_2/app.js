// my current age
//const myAge=24;
const myAge=24.5;
// early dog years
let earlyYears=2;
earlyYears*=10.5;
// my age from third year onwards
let laterYears=myAge-2;
// my age in dog years from third year onwards
laterYears*=4;
console.log(`earlyYears=${earlyYears}; laterYears=${laterYears}`);
const myAgeInDogYears=earlyYears+laterYears;
console.log(`myAgeInDogYears=${myAgeInDogYears}`);
// using a string method now
let myName="AhiYantra";
myName=myName.toLowerCase();
// logging everything to the console in a single statement
console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`);