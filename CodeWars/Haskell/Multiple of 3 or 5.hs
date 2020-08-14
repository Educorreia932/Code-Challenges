module MultiplesOf3And5 where

solution :: Integer -> Integer
solution i = sum [x | x <- [0 .. i - 1], x `mod` 3 == 0  || x `mod` 5 == 0]