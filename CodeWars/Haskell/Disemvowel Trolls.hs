module Disemvowel where

disemvowel :: String -> String
disemvowel [] = []
disemvowel (x:xs)
  | not( x `elem` "aeiouAEIOU") = x: disemvowel  xs
  | otherwise = disemvowel  xs
