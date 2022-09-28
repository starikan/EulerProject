import { factorsOfNumber, properDivisors, sieveOfAtkin, sumArithmeticSequence } from './math';

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

  it('Собственные делители числа', () => {
    expect(properDivisors(1)).toEqual([]);
    expect(properDivisors(3)).toEqual([1]);
    expect(properDivisors(6)).toEqual([1, 2, 3]);
    expect(properDivisors(10)).toEqual([1, 2, 5]);
    expect(properDivisors(15)).toEqual([1, 3, 5]);
    expect(properDivisors(21)).toEqual([1, 3, 7]);
    expect(properDivisors(28)).toEqual([1, 2, 4, 7, 14]);
  });

  it('Сумма арифметической прогрессии', () => {
    expect(sumArithmeticSequence(1, 1, 1)).toEqual(1);
    expect(sumArithmeticSequence(1, 10, 1)).toEqual(55);
  });

  it('Решето Аткинса', () => {
    expect(sieveOfAtkin(100)).toEqual([
      2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    ]);
  });
});
