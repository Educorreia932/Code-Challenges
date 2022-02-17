import Data.List (sort)

digits :: Int -> [Int]
digits n = map (\x -> read [x] :: Int) (show n)

concatNumbers :: [Int] -> Int
concatNumbers = read . concatMap show

isPandigital :: Int -> Bool
isPandigital n = sort (digits n) == [1 .. 9] && length (show n) == 9

main :: IO ()
main = print $ maximum $ filter isPandigital [concatNumbers [x, (2 * x)] | x <- [9123 .. 9876]]