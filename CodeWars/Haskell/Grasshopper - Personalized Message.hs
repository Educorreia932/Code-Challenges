module PersonalisedGreeting (greet) where

greet :: String -> String -> String
greet name owner | name == owner = "Hello boss"
                 | otherwise = "Hello guest"