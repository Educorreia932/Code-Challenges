slice :: [a] -> Int -> Int -> [a]
slice [] _ _ = []
slice (x:xs) _ 0 = []
slice (x:xs) 1 end = x : slice xs 1 (end - 1)
slice (x:xs) start end = slice xs (start - 1) (end - 1)