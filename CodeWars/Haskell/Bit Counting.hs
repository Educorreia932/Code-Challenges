module BitCounting (countBits) where

toBinary :: Int -> [Int]
toBinary 0 = [0]
toBinary n = toBinary (n `quot` 2) ++ [n `rem` 2]

countBits :: Int -> Int
countBits i = length $ filter(==1) $ toBinary i