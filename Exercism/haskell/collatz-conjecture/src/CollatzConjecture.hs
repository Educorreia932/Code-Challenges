module CollatzConjecture (collatz) where

import Data.Maybe (fromMaybe)

collatz :: Integer -> Maybe Integer
collatz n
    | n < 1 = Nothing
    | n == 1 = Just 0
    | otherwise = succ <$> collatz' n
  where
    collatz' x
        | even x = collatz (x `div` 2)
        | otherwise = collatz (3 * x + 1)
