import Data.ByteString (cons)
import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

isPrime :: Int -> Bool
isPrime n = not $ any (\x -> n `mod` x == 0) [2..isqrt $ abs n]

consecutivePrimes :: Int -> Int -> Int
consecutivePrimes a b = fromMaybe 0 (False `elemIndex` map (\n -> isPrime $ n ^ 2 + a * n + b) [0..])

main :: IO()
main = print $ product $ tail $ maximum $ [[consecutivePrimes x y, x, y] | x <- [-999..999], y <- [-1000..1000]]
