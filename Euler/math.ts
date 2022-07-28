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

// Решето Аткинса
export const sieveOfAtkin = (limit: number): number[] => {
  // Initialise the sieve array with false values
  let sieve: boolean[] = new Array(limit + 1).fill(false);

  // 2 and 3 are known to be prime
  if (limit > 2) {
    sieve[2] = true;
  }
  if (limit > 3) {
    sieve[3] = true;
  }

  /* Mark sieve[n] is true if one of the following is true:
    a) n = (4*x*x)+(y*y) has odd number of solutions, i.e., there exist odd number of distinct pairs (x, y) that satisfy the equation and n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has odd number of solutions and n % 12 = 7
    c) n = (3*x*x)-(y*y) has odd number of solutions, x > y and n % 12 = 11
  */
  for (let x = 1; x * x <= limit; x += 1) {
    for (let y = 1; y * y <= limit; y += 1) {
      let n = 4 * x * x + y * y;
      if (n <= limit && (n % 12 === 1 || n % 12 === 5)) {
        sieve[n] = !sieve[n];
      }

      n = 3 * x * x + y * y;
      if (n <= limit && n % 12 === 7) {
        sieve[n] = !sieve[n];
      }

      n = 3 * x * x - y * y;
      if (x > y && n <= limit && n % 12 === 11) {
        sieve[n] = !sieve[n];
      }
    }
  }

  // Mark all multiples of squares as non-prime
  for (let r = 5; r * r <= limit; r++) {
    if (sieve[r]) {
      for (let i = r * r; i <= limit; i += r * r) {
        sieve[i] = false;
      }
    }
  }

  return sieve.map((v, i) => (v ? i : v)).filter((v) => !!v) as number[];
};
