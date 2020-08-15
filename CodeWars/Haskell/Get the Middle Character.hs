module Codewars.G964.Getmiddle where

getMiddle :: String -> String
getMiddle [] = []
getMiddle xs | odd (length xs) = [xs !! ((length xs) `div` 2)]
             | otherwise = [(reverse $ xs) !! ((length xs)`div` 2), (xs !! ((length xs) `div` 2))]