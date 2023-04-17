// Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

// Example 1:


// Input: points = [[1,1],[2,2],[3,3]]
// Output: 3
// Example 2:


// Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
// Output: 4

// Constraints:

// 1 <= points.length <= 300
// points[i].length == 2
// -104 <= xi, yi <= 104
// All the points are unique.


/**
Дан массив точек points, где points[i] = [xi, yi] представляют собой координаты точек на плоскости X-Y. Найти максимальное количество точек которые лежат на одной прямой.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Ограничения:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
Все точки уникальны.
 */

// function maxPoints(points: number[][]): number {
// }


function maxPoints(points: number[][]): number {
  let maxLen = 1;
  for (let i = 0; i < points.length; i++) {
    const startPoint = points[i];
    for (let j = i + 1; j < points.length; j++) {
      const nextPoint = points[j];

      let acc = [startPoint, nextPoint];

      for (let k = j + 1; k < points.length; k++) {
        const checkPoint = points[k];
        const check =
          (checkPoint[0] - startPoint[0]) * (nextPoint[1] - startPoint[1]) ===
          (checkPoint[1] - startPoint[1]) * (nextPoint[0] - startPoint[0]);
        if (check) {
          acc.push(checkPoint);
        }
      }

      if (acc.length > maxLen) {
        maxLen = acc.length;
      }
    }
  }
  return maxLen;
}

console.log(
  maxPoints([
    [1, 1],
    [2, 2],
    [3, 3],
  ]),
);
console.log(
  maxPoints([
    [1, 1],
    [3, 2],
    [5, 3],
    [4, 1],
    [2, 3],
    [1, 4],
  ]),
);
console.log(
  maxPoints([
    [2, 3],
    [3, 3],
    [-5, 3],
  ]),
);
console.log(
  maxPoints([
    [0, 0],
    [1, -1],
    [1, 1],
  ]),
);
