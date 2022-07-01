/*
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
*/

function transformNumberToLetters(num: number): string {
  const a = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
  ];
  const b = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];

  const pairs = [...a];
  for (let i = 20; i < 100; i++) {
    const first = Math.floor(i / 10);
    const second = i - Math.floor(i / 10) * 10;
    pairs.push(`${b[first]}${second ? '-' : ''}${second ? a[second] : ''}`);
  }

  if (num > 9999) {
    throw new Error(`Invalid number: ${num}`);
  }

  const thousands = Math.floor(num / 1000);
  const hundreds = Math.floor((num - thousands * 1000) / 100);
  const tens = Math.floor(num - thousands * 1000 - hundreds * 100);

  const result = [
    thousands ? `${pairs[thousands]} thousand` : '',
    thousands && hundreds ? ' and ' : '',
    hundreds ? `${pairs[hundreds]} hundred` : '',
    hundreds && tens ? ' and ' : '',
    tens ? pairs[tens] : '',
  ];
  return result.join('');
}

let sum = 0;
for (let i = 1; i <= 1000; i++) {
  const s = transformNumberToLetters(i);
  sum = sum + s.replace(/[\s-]/g, '').length;
}
console.log(sum);
