{-# LANGUAGE OverloadedStrings #-}

import Data.Char (isDigit)
import Data.Function (on)
import Data.List (sort, sortBy)
import Data.Map qualified as Map
import Data.Text qualified as Text

data Color = Red | Green | Blue deriving (Show, Eq, Ord)
type Set = Map.Map Color Integer
type Game = [Set]

parseInput :: String -> [Game]
parseInput xs = map (parseGame . Text.splitOn ";" . Text.pack . tail . dropWhile (':' /=)) (lines xs)
 where
  parseColor :: Text.Text -> Color
  parseColor "red" = Red
  parseColor "green" = Green
  parseColor "blue" = Blue
  parseColor _ = error "Invalid color"

  parseSet :: [Text.Text] -> Set
  parseSet xs = Map.fromList $ foldl (\acc x -> acc ++ [parseItem x]) [] xs
   where
    parseItem x =
      let (_ : quantity : color : _) = Text.splitOn " " x
       in (parseColor color, read $ Text.unpack quantity :: Integer)

  parseGame :: [Text.Text] -> Game
  parseGame [] = []
  parseGame (x : xs) = parseSet (Text.splitOn "," x) : parseGame xs

part1 :: [Game] -> Integer
part1 = sum . map fst . filter snd . zip [1 ..] . map (all isSetValid)
 where
  isSetValid xs =
    all
      ( \(color, quantity) ->
          (quantity <= 12 && color == Red)
            || (quantity <= 13 && color == Green)
            || (quantity <= 14 && color == Blue)
      )
      (Map.toList xs)

part2 :: [Game] -> Integer
part2 = sum . map (setPower . minimumBalls . map completeSet)
 where
  completeSet :: Set -> Set
  completeSet set = foldr (\color -> Map.insertWith (+) color 0) set [Green, Red, Blue]

  minimumBalls :: Game -> Set
  minimumBalls game = foldr mergeMap (head game) (tail game)
   where
    mergeMap = Map.unionWith max

  setPower :: Set -> Integer
  setPower set = product $ map snd (Map.toList set)

main :: IO ()
main = do
  input <- parseInput <$> readFile "input"
  print $ part1 input
  print $ part2 input
