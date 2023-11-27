module Anagram (anagramsFor) where

import Data.Char (toLower)
import Data.List (sort)

anagramsFor :: String -> [String] -> [String]
anagramsFor xs = filter (isAnagram xs)

isAnagram :: String -> String -> Bool
isAnagram s1 s2 = normalize s1 == normalize s2 && map toLower s1 /= map toLower s2
  where
    normalize = sort . map toLower