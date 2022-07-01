import { factorsOfNumber, sumArithmeticSequence } from './math';

describe('Math helpers', () => {
  it('Делители числа', () => {
    expect(factorsOfNumber(1)).toEqual([1]);
    expect(factorsOfNumber(3)).toEqual([1, 3]);
    expect(factorsOfNumber(6)).toEqual([1, 2, 3, 6]);
    expect(factorsOfNumber(10)).toEqual([1, 2, 5, 10]);
    expect(factorsOfNumber(15)).toEqual([1, 3, 5, 15]);
    expect(factorsOfNumber(21)).toEqual([1, 3, 7, 21]);
    expect(factorsOfNumber(28)).toEqual([1, 2, 4, 7, 14, 28]);
  });

  it('Сумма арифметической прогрессии', () => {
    expect(sumArithmeticSequence(1, 1, 1)).toEqual(1);
    expect(sumArithmeticSequence(1, 10, 1)).toEqual(55);
  })
});
