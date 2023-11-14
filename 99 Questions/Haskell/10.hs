encode :: Eq a => [a] -> [(Int, a)]
encode [] = []
encode list = (length start, head start) : encode rest
    where (start, rest) = span (== head list) list