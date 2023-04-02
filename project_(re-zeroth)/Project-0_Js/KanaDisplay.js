const kanaDisplay = document.getElementById("kana-display");
const kanaList = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん"];
		
function getRandomKana() {
	// return kanaList[Math.floor(Math.random() * kanaList.length)];

	// Generate a random number between the kana unicode range
	const min = parseInt("3040", 16);
	const max = parseInt("309F", 16);
	const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;

	// Convert the number to its corresponding character
	const kanaSymbol = String.fromCharCode(randomNumber);

	// Update the display with the new symbol
	//document.getElementById("kana-display").innerHTML = kanaSymbol;

	return kanaSymbol;
}
		
function updateKana() {
	kanaDisplay.innerText = getRandomKana();
}

updateKana();
		
setInterval(updateKana, 60000);
		
function closeWindow() {
	window.close();
}
		
function updateKanaAgain() {
	kanaDisplay.innerText = getRandomKana();
}