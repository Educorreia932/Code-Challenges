module DNA (toRNA) where

toRNA :: String -> Either Char String
toRNA [] = Right []
toRNA (x:xs)
    | x == 'G' = toRNA xs >>= (\ys -> Right ('C':ys)) -- G -> C
    | x == 'C' = toRNA xs >>= (\ys -> Right ('G':ys)) -- C -> G
    | x == 'T' = toRNA xs >>= (\ys -> Right ('A':ys)) -- T -> A
    | x == 'A' = toRNA xs >>= (\ys -> Right ('U':ys)) -- A -> U
    | otherwise = Left x
