import Foundation

for _ in 0..<Int(readLine()!)! {
  let arr = readLine()!.components(separatedBy: ",")
  print(Int(arr[0])! + Int(arr[1])!)
}