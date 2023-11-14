compress :: (Eq a) => [a] -> [a]
compress list = foldl (\acc x -> acc ++ ([x | x /= last acc])) [head list] list