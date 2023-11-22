repli :: [a] -> Int -> [a]
repli list n = concatMap (replicate n) list
