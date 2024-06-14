//
//  bj_2914.swift
//  swft
//
//  Created by 박동현 on 6/14/24.
//

import Foundation

let num = readLine()!.components(separatedBy : " ")

let ans = (Int(num[0])!) * (Int(num[1])!-1)
print(Int(ans)+1)
