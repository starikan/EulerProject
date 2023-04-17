/**
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
*/


/**
Дан массив уникальных целых чисел candidates и целое число target. Вернуть список всех уникальных комбинаций чисел из candidates, сумма которых равна target. Комбинации могут быть в любом порядке.
Одно и то же число из candidates может быть выбрано неограниченное количество раз.
Две комбинации считаются уникальными, если частота хотя бы одного из выбранных чисел отличается.
Тестовые случаи генерируются таким образом, что количество уникальных комбинаций, сумма которых равна target, меньше 150 комбинаций для данного входного значения.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Объяснение:
* 2 и 3 являются кандидатами, и 2 + 2 + 3 = 7. Обратите внимание, что число 2 может быть использовано несколько раз.
* 7 является кандидатом, и 7 = 7.
Это единственные две комбинации.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Ограничения:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
Все элементы candidates различны.
1 <= target <= 40
 */


function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function backtrack(start: number, currSum: number, path: number[]): void {
      if (currSum === target) {
          result.push([...path]); // Append a copy of the path to the result
          return;
      } else if (currSum > target) {
          return;
      }

      for (let i = start; i < candidates.length; i+=1) {
          path.push(candidates[i]);
          backtrack(i, currSum + candidates[i], path); // Use the current candidate
          path.pop(); // Backtrack by removing the last added element
      }
  }

  candidates.sort((a, b) => a - b); // Sort the candidates to avoid duplicates and optimize backtracking
  backtrack(0, 0, []);
  return result;
}

console.log(combinationSum([2, 3, 6, 7], 7));
console.log(combinationSum([2, 3, 5], 8));
console.log(combinationSum([2], 1));
