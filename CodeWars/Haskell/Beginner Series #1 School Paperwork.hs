module Codewars.Kata.Paperwork where

paperwork :: Int -> Int -> Int
paperwork m n | m < 0 || n < 0 = 0
              | otherwise = m * n