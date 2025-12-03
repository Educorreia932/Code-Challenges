import Data.Char (digitToInt)

type BatteryBank = [Int]

parseInput :: String -> [BatteryBank]
parseInput = map (map digitToInt) . lines

largestJoltage :: BatteryBank -> Int -> Int
largestJoltage bank@(b : bs) n =
  fromDigits . take n . fst $ foldl step ([b], 0) bs
  where
    maxToRemove = length bank - n

    fromDigits :: [Int] -> Int
    fromDigits = read . concatMap show

    step :: (BatteryBank, Int) -> Int -> (BatteryBank, Int)
    step (bank, numRemoved) battery =
      let (bank', removed') = removeLowerBatteries bank numRemoved
       in (bank' ++ [battery], removed')
      where
        removeLowerBatteries :: BatteryBank -> Int -> (BatteryBank, Int)
        removeLowerBatteries bank numRemoved
          | not $ null bank,
            last bank < battery,
            numRemoved < maxToRemove =
              removeLowerBatteries (init bank) (numRemoved + 1)
          | otherwise = (bank, numRemoved)

partOne :: [BatteryBank] -> Int
partOne = sum . map (`largestJoltage` 2)

partTwo :: [BatteryBank] -> Int
partTwo = sum . map (`largestJoltage` 12)

main :: IO ()
main = do
  input <- parseInput <$> readFile "input"
  putStrLn $ "Part 1: " ++ show (partOne input)
  putStrLn $ "Part 2: " ++ show (partTwo input)
