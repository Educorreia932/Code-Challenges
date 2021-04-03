module WarnSheep (warnTheSheep) where

import Data.List
import Data.Maybe

warnTheSheep :: [String] -> String
warnTheSheep xs | i == 0 = "Pls go away and stop eating my sheep"
                | otherwise = "Oi! Sheep number " ++ show i ++ "! You are about to be eaten by a wolf!"   
                where i = fromJust $ elemIndex "wolf" (reverse xs)  
