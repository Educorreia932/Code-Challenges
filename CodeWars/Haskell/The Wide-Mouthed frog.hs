module Kata (mouthSize) where

import Data.Char (toLower)

mouthSize :: String -> String
mouthSize animal | map toLower animal == "alligator" = "small"
                 | otherwise = "wide"
