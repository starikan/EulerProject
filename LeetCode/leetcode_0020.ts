// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.


// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false


// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.



/**
Дана строка, состоящая исключительно из символов '(', ')', '{', '}', '[', ']'.
Проверить валидность строки.
Валидность означает:
- Скобка открытия должна иметь скобку закрытия.
- Открывающие скобки должны закрываться в правильном порядке.
- Каждая закрывающая скобка имеет соответствующую открытую скобку того же типа.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Ограничения:
1 <= s.length <= 104
s содержит только символы '()[]{}'.
*/

// function isValid(s) {
//   return true;
// }

// console.log(isValid("()") === true);
// console.log(isValid("()[]{}") === true);
// console.log(isValid("(]") === false);
// console.log(isValid("([)]") === false);



function isValid(s: string): boolean {
  let len = s.length;
  while (true) {
    s = s.replace(/\{\}/g, '').replace(/\[\]/g, '').replace(/\(\)/g, '');
    if (len === s.length) {
      break;
    }
    len = s.length;
  }
  return !s.length;
}

// function isValid(s: string): boolean {
//   const stack: string[] = [];
//   const mapping: { [key: string]: string } = { ')': '(', '}': '{', ']': '[' }; // mapping for closing and opening brackets

//   for (let char of s) {
//       if (char in mapping) { // if it's a closing bracket
//           const topElement = stack.pop() || '#'; // get the top element from the stack, or use '#' as a dummy value if stack is empty
//           if (mapping[char] !== topElement) { // check if the popped element matches the corresponding opening bracket
//               return false;
//           }
//       } else {
//           stack.push(char); // if it's an opening bracket, push it to the stack
//       }
//   }

//   return !stack.length; // if stack is empty after processing all characters, return true, else false
// }

// function isValid(s: string): boolean {
//   let openCount = 0;
//   const openBrackets = '([{';
//   const closeBrackets = ')]}';

//   for (let char of s) {
//       if (openBrackets.indexOf(char) !== -1) {
//           openCount++; // increment the counter for open brackets
//       } else if (closeBrackets.indexOf(char) !== -1) {
//           openCount--; // decrement the counter for close brackets
//           if (openCount < 0 || openBrackets.indexOf(s[s.length - 1]) !== closeBrackets.indexOf(char)) {
//               return false; // if the counter is negative or the corresponding open bracket doesn't match, return false
//           }
//       }
//   }

//   return openCount === 0; // if the counter is zero, return true, else false
// }



// function isValid(s: string): boolean {
//   const stack: string[] = [];
//   const mapping: Record<string, string> = {
//       "(": ")",
//       "[": "]",
//       "{": "}"
//   };

//   for (let i = 0; i < s.length; i++) {
//       const char = s.charAt(i);

//       if (mapping[char]) { // If the character is an opening bracket
//           stack.push(char);
//       } else { // If the character is a closing bracket
//           const lastChar = stack.pop();

//           if (mapping[lastChar] !== char) {
//               return false;
//           }
//       }
//   }

//   return stack.length === 0; // If the stack is empty, it means all opening brackets were closed
// }

// We first initialize an empty stack and a mapping of opening brackets to their corresponding closing brackets.
// We then iterate over each character in the input string.
// If the character is an opening bracket, we push it onto the stack.
// If the character is a closing bracket, we check if the top of the stack has the corresponding opening bracket.
// If it does, we pop the opening bracket from the stack. If it doesn't, we know that the input string is invalid and return false.

// After iterating over all characters in the input string, we check if the stack is empty.
// If it is, it means all opening brackets were closed and we return true. If it's not,
// it means there were some opening brackets that were not closed and we return false.