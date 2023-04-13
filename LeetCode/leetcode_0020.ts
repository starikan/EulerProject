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

