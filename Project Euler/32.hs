import Data.List (sort)
import Data.Set (fromList) 

digits :: Int -> [Int]
digits n = map (\x -> read [x] :: Int) (show n)

concatNumbers :: [Int] -> Int
concatNumbers = read . concatMap show

isPandigital :: Int -> Bool
isPandigital n = sort (digits n) == [1..9] && length (show n) == 9

pandigitalProducts :: [Int] -> [Int] -> [Int]
pandigitalProducts a b = [x * y | x <- a, y <- b, isPandigital $ concatNumbers [x, y, x * y]]

main :: IO()
main = print $ sum $ fromList $ pandigitalProducts [12..98] [123..987] ++ pandigitalProducts [1..9] [1234..9876]
