-- WIP 

module Reverse where

reverseWords :: String -> String
reverseWords s = unwords $ map (reverse) $ words s