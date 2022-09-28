const start = [1, 2, 1];
const triangle = [[], [1], start];

const RANGE = 20;

for (let i = 2; i <= RANGE; i += 1) {
  triangle.push([1, ...triangle[i].map((v, k, arr) => v + Number(arr[k + 1] || 0))]);
}

const result = triangle[20].map((v) => v * v).reduce((s, v) => s + v, 0);

console.log(result)