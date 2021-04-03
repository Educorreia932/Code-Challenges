module Codewars.Kata.AlternatingCase where  

import Data.Char

toAlternatingCase :: String -> String 
toAlternatingCase = map (\c -> if isLower c then toUpper c; else toLower c)
