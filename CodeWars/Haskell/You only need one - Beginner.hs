module Need where

check :: Eq a => [a] -> a -> Bool
check array value = value `elem` array