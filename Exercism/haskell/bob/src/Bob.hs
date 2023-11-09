module Bob (responseFor) where

import Data.Char (isAlpha, isLetter, isSpace, isUpper)

responseFor :: String -> String
responseFor query
    | isSilent = "Fine. Be that way!"
    | isQuestion && isYelled = "Calm down, I know what I'm doing!"
    | isQuestion = "Sure."
    | isYelled = "Whoa, chill out!"
    | otherwise = "Whatever."
  where
    isSilent = all isSpace query
    isQuestion = last (filter (not . isSpace) query) == '?'
    isYelled = all isUpper (filter isAlpha query) && any isLetter query
