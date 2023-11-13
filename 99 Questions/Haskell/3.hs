elementAt :: [a] -> Int -> a
elementAt [] _ = error "Index out of bounds"
elementAt (x : _) 1 = x
elementAt (_ : xs) i
    | i < 1 = error "Index out of bounds"
    | otherwise = elementAt xs (i - 1)