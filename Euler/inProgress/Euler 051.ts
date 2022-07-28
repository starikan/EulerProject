import { sieveOfAtkin } from '../math';

// console.log(sieveOfAtkin(100));

function combinations<T>(set: Array<T>, k: number): Array<Array<T>> {
  // src: https://gist.github.com/axelpale/3118596
  if (k > set.length || k <= 0) return [];
  if (k === set.length) return [set];
  if (k === 1) return set.map((x) => [x]);

  return set.reduce((p, c, i) => {
    combinations(set.slice(i + 1), k - 1).forEach((tailArray) => p.push([c, ...tailArray]));

    return p;
  }, [] as T[][]);
}

const getAllCombinations = (digitsCount: number) => {
  const arr = [...Array(digitsCount + 1).keys()].filter((v) => v);
  const arrPositions = [...Array(digitsCount).keys()];
  const comb = arr.map((v, i) => combinations(arrPositions, i));
  return comb;
};

const digits = [...Array(10).keys()];

for (let i = 1000; i < 1010; i++) {
  const str = String(i).split('');
  const combs = getAllCombinations(str.length);
  for (const comb of combs) {
    const results = [];
    for (const digit of digits) {
      for (const places of comb) {
        for (const place of places) {
          results.push();
        }
      }
    }
    // const replaces = comb.map(v => v.map(d => String(i)[]))
  }
  console.log(combs);
}

debugger;
