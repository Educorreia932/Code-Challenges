module SumOfMultiples (sumOfMultiples) where

import Data.List (nub)

sumOfMultiples :: [Integer] -> Integer -> Integer
sumOfMultiples factors limit = sum $ nub $ concatMap (multiples limit) factors
  where
    multiples _ 0 = [0]
    multiples limit n = takeWhile (< limit) $ iterate (+ n) 0
