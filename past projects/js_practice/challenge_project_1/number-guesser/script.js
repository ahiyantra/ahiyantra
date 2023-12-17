let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => {
  let randInt = Math.floor(Math.random()*9);
  return randInt;
}

const compareGuesses = (human, computer, target) => {
  let humanDiff=Math.abs(target-human);
  let computerDiff=Math.abs(target-computer);
  if (human < 0 || human > 9) {
    alert('Your chosen number is out of range! Please choose a number between 0 and 9!');
  } else if (humanDiff<=computerDiff) {
    return true;
  } else {
    return false;
  }
}

const updateScore = winner => {
  if (winner==='human') {
    humanScore+=1;
  } else {
    computerScore+=1;
  }
}

const advanceRound = () => {
  currentRoundNumber+=1;
}