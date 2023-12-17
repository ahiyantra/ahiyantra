const getSleepHours = day => {
  switch(day) {
    case 'monday':
      return 8;
      break;
    case 'tuesday':
      return 7;
      break;
    case 'wednesday':
      return 6;
      break;
    case 'thursday':
      return 5;
      break;
    case 'friday':
      return 4;
      break;
    case 'saturday':
      return 3;
      break;
    case 'sunday':
      return 9;
      break;
  }
}

//console.log(getSleepHours('sunday'));

const getActualSleepHours = () => getSleepHours('sunday') + getSleepHours('monday') + getSleepHours('tuesday') + getSleepHours('wednesday') + getSleepHours('thursday') + getSleepHours('friday') + getSleepHours('saturday');

//console.log(getActualSleepHours());

const getIdealSleepHours = (idealHours=6) => {
  return idealHours*7;
}

//console.log(getIdealSleepHours());

const calculateSleepDebt = () => {
  let actualSleepHours=getActualSleepHours();
  let idealSleepHours=getIdealSleepHours(6);
  if (actualSleepHours===idealSleepHours) {
    return 'The user got the perfect amount of sleep.';
  } else if (actualSleepHours>idealSleepHours) {
    let extra=actualSleepHours-idealSleepHours;
    return 'The user got more sleep than needed. They slept '+extra+' hours extra.';
  } else {
    let lack=idealSleepHours-actualSleepHours;
    return 'The user should get some rest. They lack '+lack+' hours of sleep.';
  }
}

console.log(calculateSleepDebt());
