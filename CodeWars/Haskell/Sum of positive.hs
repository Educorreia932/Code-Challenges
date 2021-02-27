module Codewars.Arrays where

positiveSum :: [Int] -> Int
positiveSum n = sum $ filter (> 0) n
