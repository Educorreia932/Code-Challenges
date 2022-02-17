fractions :: [(Int, Int)]
fractions = [(n, d) | n <- [1 .. 7], d <- [n .. 8], c <- [d .. 9], 9 * n * (c - d) == c * (d - n) && c /= d && c /= n && d /= n]

reduceFraction :: Integral a => (a, a) -> a
reduceFraction (n, d) = d `div` (gcd n d)

main :: IO ()
main = print $ reduceFraction $ foldr1 (\(n, d) (n', d') -> (n * n', d * d')) fractions
