const n = 13;
const k = 3;

let circle = new Array(n).fill(0).map((v, i) => i);

debugger
while(circle.length>1) {
  const newK = circle.length % k
  circle = circle.filter((v, i) => i%k)
  debugger
}
// let i = 0;
// let step = 1000;
// while (circle.length > 1 && step > 0) {
//   circle.splice(i, 1);
//   debugger;
//   i += k;
//   if (i > circle.length) {
//     i = circle.length - i;
//   }
//   step--;
// }
debugger;
