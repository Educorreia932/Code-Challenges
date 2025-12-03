parseInput :: String -> [Int]
parseInput = map parseRotation . lines

parseRotation :: String -> Int
parseRotation (c : cs) = if c == 'L' then (-delta) else delta
  where
    delta = read cs

rotateDial :: Int -> Int -> Int
rotateDial position delta = (position + delta) `mod` 100

partOne :: [Int] -> Int
partOne =
  length
    . filter (== 0)
    . tail
    . scanl rotateDial 50

partTwo :: [Int] -> Int
partTwo =
  snd
    . foldl
      ( \(position, password) delta ->
          let password' =
                password
                  + if delta >= 0
                    then (position + delta) `div` 100
                    else (((100 - position) `mod` 100) - delta) `div` 100
           in (rotateDial position delta, password')
      )
      (50, 0)

main :: IO ()
main = do
  input <- parseInput <$> readFile "input"
  putStrLn $ "Part 1: " ++ show (partOne input)
  putStrLn $ "Part 2: " ++ show (partTwo input)
