module Pangram (isPangram) where
import Data.Char (toLower, isAlpha)
import Data.List (nub, sort)

isPangram :: String -> Bool
isPangram text = all (`elem` map toLower text) ['a'..'z']
