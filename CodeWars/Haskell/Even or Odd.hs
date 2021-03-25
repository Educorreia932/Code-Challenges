module EvenOrOdd where

evenOrOdd :: Integral a => a -> [Char]
evenOrOdd n | even n = "Even"
            | otherwise = "Odd"