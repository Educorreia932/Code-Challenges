module Codewars.Kata.IsUpperCase where

import Data.Char

isUpperCase :: String -> Bool
isUpperCase str = map toUpper str == str
