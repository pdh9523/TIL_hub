import Foundation


let line = readLine()!
let arr = line.components(separatedBy :" ")

let a = Int(arr[0])!
let b = Int(arr[1])!
let c = Int(arr[2])!
let d = Int(arr[3])!
let e = Int(arr[4])!

var ans = a*a+b*b+c*c+d*d+e*e

print(ans%10)