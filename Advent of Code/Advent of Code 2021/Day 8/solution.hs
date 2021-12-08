import Data.List.Split(splitOn)
import Data.List (intercalate)

parseInput = map $ map words . splitOn "|"
partOne = sum . map (\x -> length $ filter (\x -> elem x [2, 3, 4, 7]) (map length $ x !! 1))

main = do
    print =<< return . partOne . parseInput . lines =<< readFile("input.txt")