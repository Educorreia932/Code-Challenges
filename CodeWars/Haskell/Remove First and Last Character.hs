module Haskell.Codewars.RemoveChar where

removeChar :: String -> String
removeChar str = take (length str - 2) (drop 1 str) 