--WIP 

module TotalPoints where

import Data.Text (replace)

score :: [Char] -> Int
score result | x > y = 3 
             | x < y = 0
             | otherwise = 1
             where 
                teamResults = map (\r -> read r :: Int) $ replace "," " " result
                x = head teamResults
                y = last teamResults

points :: [String] -> Int
points results = sum $ map results () 
