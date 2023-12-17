const getUserChoice = userInput => {
  userInput=userInput.toLowerCase();
  if(userInput==='rock'||userInput==='paper'||userInput==='scissors'||userInput==='bomb') {
    return userInput;
  } else {
    return 'Please enter a valid input.';
  }
}

//console.log('user\'s choice: '+getUserChoice('bronze'));

const getComputerChoice = () => {
  n=Math.floor(Math.random()*3);
  if(n===0) {
    return 'rock';
  } else if(n===1) {
    return 'paper';
  } else {
    return 'scissors';
  }
}

const determineWinner = (userChoice, computerChoice) => {
  if(userChoice===computerChoice) {
    return 'The game was a tie.';
  } else if(userChoice==='bomb') {
    return 'User won by default.';
  } else if(userChoice==='rock') {
    if(computerChoice==='paper') {
      return 'Computer won.';
    } else {
      return 'User won.';
    }
  } else if(userChoice==='paper') {
    if(computerChoice==='scissors') {
      return 'Computer won.';
    } else {
      return 'User won.';
    }
  } else if(userChoice==='scissors') {
    if(computerChoice==='rock') {
      return 'Computer won.';
    } else {
      return 'User won.';
    }
  }
}


const playGame = () => {
  let userChoice=getUserChoice('bomb');
  let computerChoice=getComputerChoice();
  console.log('user\'s choice: '+userChoice);
  console.log('computer\'s choice: '+computerChoice);
  console.log(determineWinner(userChoice,computerChoice));
}

playGame();
