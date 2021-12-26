function fiboEvenSum(n) {
  let sum = 0, f1 = 0, f2 = 1, f3 = 0 , i = 1
  while(n >= i){
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if (f3 % 2 == 0 && f3 <= n){
      sum += f3
    }
    i++
  } 
  return sum;
}
