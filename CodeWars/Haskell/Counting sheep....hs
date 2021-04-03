module Codewars.Kata.Sheep where

countSheep :: [Bool] -> Int
countSheep xs = length $ filter id xs
