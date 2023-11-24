module Acronym (abbreviate) where

import Data.Char (isAlpha, isUpper, toLower, toUpper)

titlecase :: String -> String
titlecase xs@(head : tail)
    | all isUpper xs = toUpper head : map toLower tail
    | otherwise = xs
titlecase [] = []

abbreviate :: String -> String
abbreviate xs = concatMap (\x -> [toUpper $ head x]) splitted
  where
    splitted = words $ concatMap replace $ unwords $ map titlecase (words xs)
    replace c
        | c == '-' || c == '_' = " "
        | isUpper c = ' ' : [c]
        | otherwise = [c]
