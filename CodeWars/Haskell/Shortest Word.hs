module FindShortest where

import Data.List (minimumBy)
import Data.Ord (comparing)

find_shortest :: String -> Integer
find_shortest [] = 0
find_shortest s = fromIntegral $ length $ minimumBy (comparing length) (words s)