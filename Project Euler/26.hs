import Data.List
import Data.Maybe

coprimeToTen :: Integer -> Integer
coprimeToTen n | even n = coprimeToTen $ n `div` 2
               | n `mod` 5 == 0 = coprimeToTen $ n `div` 5
               | otherwise = n

eqn :: Integer -> Int
eqn 1 = 0
eqn n' = 1 + fromMaybe 0 (elemIndex 1 $ map (\k -> 10 ^ k `mod` n') [1..])

main :: IO() 
main = print $ maximum $ map (eqn . coprimeToTen) [1..1000]

