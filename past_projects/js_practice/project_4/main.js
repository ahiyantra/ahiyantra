let raceNumber = Math.floor(Math.random() * 1000);

const registeredEarly=true;

const runnerAge=18;

if (runnerAge>18 && registeredEarly===true) {
  raceNumber+=1000;
}

if (runnerAge>18 && registeredEarly===true) {
  console.log(`Those who were registered early & are older than 18 will race at 09:30 AM! Your race number is ${raceNumber}.`);
} else if (runnerAge>18 && registeredEarly!==true) {
  console.log(`Those who were registered late & are older than 18 will race at 11:00 AM! Your race number is ${raceNumber}.`);
} else if (runnerAge<18) {
  console.log(`Those with ages below 18 will race at 12:30 PM! Your race number is ${raceNumber}.`);
} else {
  console.log('Please see the registration desk.');
}