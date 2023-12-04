{-# LANGUAGE OverloadedStrings #-}

import Data.Char (isDigit)
import Data.List (intersect)
import Data.Text qualified as Text

type Numbers = [String]
type Card = (Numbers, Numbers)

parseInput :: String -> [Card]
parseInput = map parseCard . lines
  where
    parseCard line =
        let n = map Text.words $ Text.splitOn "|" $ Text.pack $ tail $ dropWhile (':' /=) line
         in (map Text.unpack $ head n, map Text.unpack $ last n)

part1 :: [Card] -> Int
part1 =
    foldl
        ( \acc (a, b) ->
            let numWins = length $ a `intersect` b
                points = if numWins /= 0 then 2 ^ (numWins - 1) else 0
             in acc + points
        )
        0

main :: IO ()
main = do
    input <- parseInput <$> readFile "input"
    print $ part1 input