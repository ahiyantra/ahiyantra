const kanjiDisplay = document.getElementById("kanji-display");

function getRandomKanji() {
  var kanjiRange = '\u4e00-\u9faf'; // Range of the kanji in unicode
  var chosenKanji = String.fromCharCode(Math.floor(Math.random() * (0x9faf - 0x4e00 + 1)) + 0x4e00);
  //kanjiDisplay.textContent = chosenKanji;

  return chosenKanji;
}
    
function updateKanji() {
  kanjiDisplay.innerText = getRandomKanji();
}

updateKanji();
    
setInterval(updateKana, 60000); // Change the kanji every minute
    
function closeWindow() {
  window.close();
}
    
function updateKanjiAgain() {
  kanjiDisplay.innerText = getRandomKanji();
}