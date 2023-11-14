pack :: Eq a => [a] -> [[a]]
pack [] = []
pack list = start : pack rest
    where (start, rest) = span (== head list) list