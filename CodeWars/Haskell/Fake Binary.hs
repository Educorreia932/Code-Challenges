module Codewars.Kata.FakeBinary where 

import Data.Char(digitToInt)

fakeBin :: String -> String
fakeBin = map (\c -> if digitToInt c < 5 then '0'; else '1')
