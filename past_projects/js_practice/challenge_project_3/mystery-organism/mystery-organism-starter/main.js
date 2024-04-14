// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G']
  return dnaBases[Math.floor(Math.random() * 4)] 
}

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = []
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase())
  }
  return newStrand
}

// New Code Below This Line

const pAequorFactory = (num, arr) => {
  return {
    specimenNum: num,
    dna: arr,
    mutate () {
      let newArr = this.dna.slice();
      let randInt = Math.floor(Math.random() * 15);
      let randBase = returnRandBase();
      do {
        randInt = Math.floor(Math.random() * 15);
        randBase = returnRandBase();
        // console.log(randInt);
        // console.log(this.dna[randInt]);
        // console.log(randBase);
        newArr[randInt] = randBase;
      } while (newArr[randInt]===this.dna[randInt]);
      this.dna=newArr;
    },
    compareDNA (obj) {
      let mainGen = this.specimenNum;
      let sideGen = obj.specimenNum; 
      let percentage=0;
      let common=0;
      for (let i=0; i<this.dna.length; i++) {
        if (this.dna[i]===obj.dna[i]) {
          common++;
        };
      };
      percentage=(common/this.dna.length)*100;
      console.log(`${mainGen} and ${sideGen} have ${percentage}% DNA in common.`)
    },
    willLikelySurvive () {
      let bool = false;
      let count = 0;
      for (let i=0; i<this.dna.length; i++) {
        if (this.dna[i]==='C'||this.dna[i]==='G') {
          count++;
        };
      };
      let percentage = (count/this.dna.length) * 100;
      if (percentage >= 60) {
        bool = true;
      };
      return bool;
    },
    complementStrand () {
      let complement = [];
      for (let i = 0; i < this.dna.length; i++) {
        if (this.dna[i]==='A') {
          complement.push('T');
        } else if (this.dna[i]==='T') {
          complement.push('A');
        } else if (this.dna[i]==='C') {
          complement.push('G');
        } else if (this.dna[i]==='G') {
          complement.push('C');
        };
      };
      return complement;
    }
  };
};

// Test Case

let newOrg = pAequorFactory(1, mockUpStrand());
let newerOrg = pAequorFactory(2, mockUpStrand());

//console.log(newOrg);
//newOrg.mutate();
//console.log(newOrg);
//newOrg.compareDNA(newerOrg);
//console.log(newOrg.willLikelySurvive());
//console.log(newerOrg.willLikelySurvive());

let sampleSet = [];
let n = 1;

do {
  let newestOrg = pAequorFactory(n, mockUpStrand());
  if (newestOrg.willLikelySurvive()===true) {
    sampleSet.push(newestOrg);
    n++
  };
} while (sampleSet.length<30);

//console.log(sampleSet.length);

//console.log(newOrg.dna);
//console.log(newOrg.complementStrand());
