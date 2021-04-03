module Kata where

repeater :: String -> Int -> String 
repeater string n = concat $ replicate n string
