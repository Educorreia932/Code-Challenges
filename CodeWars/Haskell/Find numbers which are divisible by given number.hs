module DivisibleBy (divisibleBy) where

divisibleBy :: [Int] -> Int -> [Int]
divisibleBy array n = filter (\x -> x `mod` n == 0) array