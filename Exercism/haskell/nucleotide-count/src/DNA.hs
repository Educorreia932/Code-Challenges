module DNA (nucleotideCounts, Nucleotide (..)) where

import Data.Map (Map, fromList)

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

count :: (Eq a) => a -> [a] -> Int
count x = length . filter (x ==)

nucleotideCounts :: String -> Either String (Map Nucleotide Int)
nucleotideCounts xs
  | all isNucleotide xs = Right $ fromList [(A, count 'A' xs), (C, count 'C' xs), (G, count 'G' xs), (T, count 'T' xs)]
  | otherwise = Left "error"
 where
  isNucleotide = (`elem` "ACGT")