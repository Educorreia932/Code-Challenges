module Strain (keep, discard) where

discard :: (a -> Bool) -> [a] -> [a]
discard p = foldr (\x acc -> if p x then acc else x : acc) []

keep :: (a -> Bool) -> [a] -> [a]
keep p = foldr (\x acc -> if p x then x : acc else acc) []
