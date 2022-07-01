//  Поиск всех делителей целого числа
export const factorsOfNumber = (n: number): number[] => {
  const result: number[] = [];
  // Note that this loop runs till square root
  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i == 0) {
      result.push(Math.round(n / i));
      result.push(i);
    }
  }

  return [...new Set(result)].sort((a, b) => a - b);
};

// Сумма арифметической прогрессии
export const sumArithmeticSequence = (start: number, count: number, step = 1): number => {
  return (start + (step * (count - 1)) / 2) * count;
};
