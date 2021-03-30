-- WIP

module Codewars.Kata.Cuboids where

findDifference :: (Int, Int, Int) -> (Int, Int, Int) -> Int
findDifference a b = abs $ product a - product b  
