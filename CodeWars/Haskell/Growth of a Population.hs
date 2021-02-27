module Codewars.G964.Arge where
import Text.Printf (printf)

nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p | p0 >= p = 0
                        | otherwise = 1 + nbYear (floor (fromIntegral p0 * (1 + percent / 100) + fromIntegral aug)) percent aug p
