import Data.List (group, sort)

mostCommon :: Ord a => [a] -> a
mostCommon = snd . maximum . map (\xs -> (length xs, head xs)) . group . sort

isInt :: Float -> Bool
isInt x = x == fromInteger (round x)

main :: IO ()
main = print $ mostCommon [floor p | a <- [1 .. 499], b <- [1 .. 499], let c = sqrt (a ^ 2 + b ^ 2), let p = a + b + c, p <= 1000, isInt c]
