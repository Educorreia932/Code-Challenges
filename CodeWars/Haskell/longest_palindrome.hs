-- WIP

module Codewars.Kata.LongestPalindrome where

isPalindrome :: String -> Int
isPalindrome s | s == reverse s = length s
               | otherwise = -1

longestPalindrome :: Eq a => [a] -> Int
longestPalindrome w = maximum (map isPalindrome $ words w)
