// return the number of 9's used to count out 1 to n
// function number9(n, start = 0) {
//   // const arr = Object.keys(Array(n + 1).fill()).join('').filter(v => v !== '9')
//   const maxNum = 2 ** 28 - 2;
//   if (n - start > maxNum) {
//     const chanks = Math.ceil(n / maxNum) - 1;
//     const edges = [
//       start,
//       ...Array(chanks)
//         .fill()
//         .map((_, i) => (i + 1) * maxNum),
//       n,
//     ];
//     debugger;

//     const summs = edges.map((v, i, array) => i < array.length && number9(array[i + 1], v));
//     console.log(summs);
//   }
//   const arr = Array.from(Array(n + 1), (_, i) => (i + start).toString().replace(/[^9]/g, '')).join('').length;
//   console.log(arr);
//   return arr;
// }

function number9(n) {
  const fractions = n
    .toString()
    .split('')
    .map((v) => parseInt(v, 10))
    .reverse()
    .map((v, i) => (i === 0 && v === 9 ? 1 : v * i * 10 ** (i-1)))
    .reduce((s, v) => s + v, 0);
  console.log(fractions);
  return fractions;
}

const run = () => {
  const assert = require('assert').strict;
  try {
    assert.equal(number9(100), 20);
  } catch (error) {
    console.log(error.message);
    debugger;
  }
  try {
    assert.equal(number9(1), 0);
  } catch (error) {
    console.log(error.message);
    debugger;
  }
  try {
    assert.equal(number9(9), 1);
  } catch (error) {
    console.log(error.message);
    debugger;
  }
  try {
    assert.equal(number9(565754), 275645);
  } catch (error) {
    console.log(error.message);
    debugger;
  }
  try {
    assert.equal(number9(10000000000), 10000000000);
  } catch (error) {
    console.log(error.message);
    debugger;
  }
};

run();
