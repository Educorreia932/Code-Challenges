module ReverseString (reverseString) where

reverseString :: String -> String
reverseString "" = ""
reverseString x = last x : reverseString (init x)
