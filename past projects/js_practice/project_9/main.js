let input='the festival is currently ongoing';
input='Hi, Human';

const vowels=['a', 'e', 'i', 'o', 'u'];

const resultArray=[];

for (letter of input) {
  //console.log(letter);
  for (vowel of vowels) {
    //console.log(vowel);
    if (letter===vowel) {
      resultArray.push(vowel);
    if (letter==='e') {
      resultArray.push('e');
    }
    if (letter==='u') {
      resultArray.push('u');
    }
    }
  }
}

console.log(resultArray.join('').toUpperCase());
