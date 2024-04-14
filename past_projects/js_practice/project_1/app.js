// the value of the variable below is staying constant
//const kelvin=293;
const kelvin=0;
// the value of the variable below is staying constant too
const celsius=kelvin-273;
// the value of the variable below is staying constant again
let farenheit=celsius*(9/5)+32;
// rounding-off the resulting value using a built-in object
farenheit=Math.floor(farenheit);
console.log(`The temperature is ${farenheit} degrees Fahrenheit.`);
// converting celsius to newton through an equation
let newton=celsius*(33/100);
// rounding-off the resulting value using a built-in object
newton=Math.floor(newton);
console.log(`The temperature is ${newton} degrees Newton.`);