let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';

let overusedWords = ['really', 'very', 'basically'];

let unnecessaryWords = ['extremely', 'literally', 'actually' ];

let storyWords = story.split(' ');

console.log('Number of words: '+storyWords.length);

let betterWords = storyWords.filter(word => {
  if (unnecessaryWords.includes(word)===false) {
    return word;
  }
});

let counterA=0;
let counterB=0;
let counterC=0;

for (let i=0; i<betterWords.length;i++) {
  if (betterWords[i]===overusedWords[0]) {
    counterA+=1;
  } else if (betterWords[i]===overusedWords[1]) {
    counterB+=1;
  } else if (betterWords[i]===overusedWords[2]) {
    counterC+=1;
  }
};

console.log('Number of overused words: '+counterA+', '+counterB+', '+counterC);

let sentenceCount = 0;

for (let i=0; i<betterWords.length; i++) {
  let lastIndex=betterWords[i].length-1;
  if ((betterWords[i][lastIndex]==='.')||(betterWords[i][lastIndex]==='!')) {
    sentenceCount+=1;
  }
}

console.log('Number of sentences: '+sentenceCount);

console.log(betterWords.join(' '));
