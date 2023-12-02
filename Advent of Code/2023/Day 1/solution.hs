{-# LANGUAGE OverloadedStrings #-}

import Data.Char (isDigit)
import Data.List (inits, isInfixOf, isPrefixOf, stripPrefix, tails)
import Data.Map qualified as Map
import Data.Text qualified as Text
import GHC.TypeError qualified as Text

parseInput :: String -> [String]
parseInput = lines

part1 :: [String] -> Integer
part1 =
    sum
        . map
            ( \x ->
                let digits = filter isDigit x
                 in read [head digits, last digits] :: Integer
            )

part2 :: [String] -> Integer
part2 =
    part1
        . map
            ( \xs ->
                Text.unpack
                    $ foldl
                        (\acc (key, value) -> Text.replace key (Text.concat [key, value, key]) acc)
                        (Text.pack xs)
                        conversion
            )
  where
    conversion :: [(Text.Text, Text.Text)]
    conversion =
        [ ("one", "1")
        , ("two", "2")
        , ("three", "3")
        , ("four", "4")
        , ("five", "5")
        , ("six", "6")
        , ("seven", "7")
        , ("eight", "8")
        , ("nine", "9")
        ]

main :: IO ()
main = do
    input <- parseInput <$> readFile "input"
    print $ part1 input
    print
        $ part2 input