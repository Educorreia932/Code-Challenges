module Chess (sameColor) where

import Data.List
import Data.Maybe

-- Returns wether a piece is located in a light square or not
getColor :: String -> Bool
getColor p = i /= j
            where
                i = odd $ fromJust $ elemIndex (head(p)) "ABCDEFGH"
                j = odd $ (read $ tail p) - 1

sameColor :: String -> String -> Bool
sameColor p1 p2 = getColor p1 == getColor p2
