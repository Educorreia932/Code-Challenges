module Mixed where

import Data.Either

sumMix :: [Either String Int] -> Int
sumMix xs = sum $ map (\l -> read l :: Int) (lefts xs) ++ rights xs
