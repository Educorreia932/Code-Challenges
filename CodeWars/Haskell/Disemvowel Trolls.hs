module Disemvowel where

disemvowel :: String -> String
disemvowel [] = []
disemvowel (x:xs)
  | x `notElem` "aeiouAEIOU" = x: disemvowel  xs
  | otherwise = disemvowel  xs
