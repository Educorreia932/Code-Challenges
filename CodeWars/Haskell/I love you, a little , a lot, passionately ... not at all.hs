module Kata (howMuchILoveYou) where

howMuchILoveYou :: Int -> String
howMuchILoveYou 0 = "not at all"
howMuchILoveYou 1 = "I love you"
howMuchILoveYou 2 = "a little"
howMuchILoveYou 3 = "a lot"
howMuchILoveYou 4 = "passionately"
howMuchILoveYou 5 = "madly"
howMuchILoveYou n = howMuchILoveYou (n `mod` 6)