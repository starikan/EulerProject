const fs = require('fs');
const path = require('path');

const generateCombinationsArrays = <T>(arrays: T[][]): T[][] => {
  const result: T[][] = [[]];

  for (const arr of arrays) {
    const currentCombinations: T[][] = [];
    for (const res of result) {
      for (const value of arr) {
        currentCombinations.push([...res, value]);
      }
    }
    result.push(...currentCombinations);
  }

  return result.filter((v) => v.length === arrays.length); // Exclude the empty combination []
};

const rotors = ['брудалпш', 'аявафс', 'деюньупч', 'рейнюх', 'щкъыдояё'].map((v) => v.split(''));

const allCombinations = generateCombinationsArrays(rotors).map((v) => v.join(''));

// Print all combinations
// console.log(allCombinations);

const filePath = path.resolve('C:\\DEV\\EulerProject\\mts30\\lemma32000words_rus_freq_dict_nomer.num');

try {
  // Read the file synchronously
  const fileContent = fs.readFileSync(filePath, { encoding: 'utf-8' }).toString();

  allCombinations.forEach((v) => {
    if (new RegExp(`\s${v}\s`).test(fileContent)) {
      console.log(v);
    }
  });

  // Output the file content
  // console.log('File content:', fileContent);
} catch (error) {
  console.error('Error reading the file:', error);
}
