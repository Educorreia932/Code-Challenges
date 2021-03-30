module Codewars.Kata.Convert where

digits :: Int -> [Int]
digits n = map (\x -> read[x] :: Int) (show n)

digitize :: Int -> [Int]
digitize n = reverse $ digits n
