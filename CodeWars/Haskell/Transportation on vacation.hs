module Codewars.G964.Rentalcarcost where

rentalCarCost :: Int -> Int
rentalCarCost d | d >= 7 = 40 * d - 50
                | d >= 3 = 40 * d - 20
                | otherwise = 40 * d
