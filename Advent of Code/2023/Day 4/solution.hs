{-# LANGUAGE OverloadedStrings #-}

import Data.Char (isDigit)
import Data.List (intersect)
import Data.Text qualified as Text

type Numbers = [String]
type Card = (Numbers, Numbers)

mapWithIndex :: (Int -> a -> b) -> [a] -> [b]
mapWithIndex = flip zipWith [0 ..]

parseInput :: String -> [Card]
parseInput = map parseCard . lines
  where
    parseCard line =
        let n = map Text.words $ Text.splitOn "|" $ last $ Text.splitOn ":" $ Text.pack line
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

part2 :: [Card] -> Int
part2 input =
    sum
        $ snd
        $ foldl
            updateCards
            (0, cards)
            wins
  where
    cards = replicate (length wins) 1
    wins =
        mapWithIndex
            ( \i (a, b) ->
                let numWins = length $ a `intersect` b
                    wonCards x = [i + 2 .. i + x + 1]
                 in wonCards numWins
            )
            input
    updateCards (n, acc) cards' = (n + 1, mapWithIndex (\i numCards -> numCards + (if (i + 1) `elem` cards' then acc !! n else 0)) acc)

main :: IO ()
main = do
    input <- parseInput <$> readFile "input"
    print $ part1 input
    print $ part2 input