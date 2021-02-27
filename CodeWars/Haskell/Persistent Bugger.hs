module Codewars.G.Persistence where

digits :: Integral x => x -> [x]
digits 0 = []
digits x = x `mod` 10 : digits (x `div` 10)

persistence :: Int -> Int
persistence n | n `div` 10 == 0 = 0
              | otherwise = 1 + persistence(product $ digits n)
