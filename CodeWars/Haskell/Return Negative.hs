module Codewars.Kata.Negative where

makeNegative :: (Num a, Ord a) => a -> a
makeNegative a | a > 0 = -a
               | otherwise = a