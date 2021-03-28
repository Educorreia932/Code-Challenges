module Codewars.Kata.Opposites where

inlove :: Int -> Int -> Bool
inlove a b = (odd a && even b) || (odd b && even a) 