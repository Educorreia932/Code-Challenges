module PIN where

getAdjacent :: Char -> [Char]
getAdjacent '1' = "124"
getAdjacent '2' = "1235"
getAdjacent '3' = "236"
getAdjacent '4' = "1457"
getAdjacent '5' = "24568"
getAdjacent '6' = "3569"
getAdjacent '7' = "478"
getAdjacent '8' = "57890"
getAdjacent '9' = "689"
getAdjacent '0' = "80"
 
getPINs :: String -> [String]
getPINs = mapM getAdjacent
