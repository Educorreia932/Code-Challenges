module Kata where

import Data.Char (ord, digitToInt)

sumDigits :: String -> Int
sumDigits s = sum $ map digitToInt s

calc :: String -> Int
calc s = sumDigits total1 - sumDigits total2
        where 
            total1 = concatMap (show . ord) s
            total2 = map (\c -> if c == '7' then '1' else c) total1

