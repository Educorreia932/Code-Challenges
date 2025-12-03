import Data.List.Split (splitOn)
import Text.Regex.PCRE ((=~))

parseInput :: String -> [(String, String)]
parseInput = map (toTuple . splitOn "-") . splitOn ","
  where
    toTuple [x, y] = (x, y)
    toTuple _ = error "Invalid range format"

sumInvalidIDs :: (String -> Bool) -> [(String, String)] -> Int
sumInvalidIDs isInvalid ranges =
  sum
    [ n
      | (i, j) <- ranges,
        n <- [read i .. read j],
        isInvalid (show n)
    ]

partOne :: [(String, String)] -> Int
partOne = sumInvalidIDs (=~ "^(.+)\\1$")

partTwo :: [(String, String)] -> Int
partTwo = sumInvalidIDs (=~ "^(.+)(\\1)+$")

main :: IO ()
main = do
  input <- parseInput <$> readFile "input"
  putStrLn $ "Part 1: " ++ show (partOne input)
  putStrLn $ "Part 2: " ++ show (partTwo input)
