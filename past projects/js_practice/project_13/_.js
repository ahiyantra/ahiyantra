
const _ = {
  clamp (num, low, up) {
    let lowerClampedValue = Math.max(num, low);
    let clampedValue = Math.min(lowerClampedValue, up);
    return clampedValue;
  },
  inRange (num, start, end) {
    if (end===undefined) {
      end=start;
      start=0;
    };
    if (start>end) {
      let temp=start;
      start=end;
      end=temp;
    };
    let isInRange = start<=num && num<end;
    return isInRange;
  },
  words (str) {
    let words = str.split(' ');
    return words;
  },
  pad (str, len) {
    if (len<=str.length) {
      return str;
    };
    let startPaddingLength = Math.floor((len-str.length)/2);
    let endPaddingLength = len-str.length-startPaddingLength;
    let paddedString=' '.repeat(startPaddingLength)+str+' '.repeat(endPaddingLength);
    return paddedString;
  },
  has (obj, key) {
    let hasValue=obj[key]!==undefined;
    return hasValue;
  },
  invert (obj) {
    let invertedObject= {};
    for (let key in obj) {
      const originalValue = obj[key];
      invertedObject[originalValue]=key;
    };
    return invertedObject;
  },
  findKey (obj, prefun) {
    for (let key in obj) {
      let value = obj[key];
      let predicateReturnValue = prefun(value);
      if (predicateReturnValue===true) {
        return key;
      }
    };
    return undefined;
  },
  drop (arr, num) {
    if (num===undefined) {
      num = 1;
    };
    let droppedArray = arr.slice(num);
    return droppedArray;
  },
  dropWhile (arr, prefun) {
    let dropNumber = arr.findIndex((elem, ind)=>!prefun(elem,ind,arr));
    let droppedArray = this.drop(arr, dropNumber);
    return droppedArray;
  },
  chunk (arr, size) {
    if (size===undefined) {
      size = 1;
    };
    let arrayChunks=[];
    for (let z=0; z<arr.length; z+=size) {
      let arrayChunk = arr.slice(z,z+size);
      arrayChunks.push(arrayChunk);
    }
    return arrayChunks;
  }
};



// Do not write or modify code below this line.
module.exports = _;