dropEvery :: [a] -> Int -> [a]
dropEvery list n = helper list n 1
  where
    helper [] _ _ = []
    helper (x : xs) n count
        | count `divides` n = helper xs n (count + 1)
        | otherwise = x : helper xs n (count + 1)
    n1 `divides` n2 = n1 `mod` n2 == 0
