module Codewars.Kata.Middle where

import Data.List ( sort, elemIndex )

gimme :: Ord a => (a, a, a) -> Int
gimme (a, b, c) = case idx of Just x -> x
                              _ -> -1
                  where arr = sort [a,b,c]
                        idx = elemIndex (arr !! 1) [a, b, c]
                   