isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

triangleNumber :: Int -> Int
triangleNumber n = (n * (n + 1)) `div` 2

divisors :: Int -> Int
divisors 1 = 1
divisors n = (length [x | x <- [2..isqrt n], n `rem` x == 0] + 1) * 2

solution :: Int -> Int
solution n | divisors t > 500 = t
           | otherwise = solution (n + 1)
           where t = triangleNumber n

main :: IO ()
main = do print $ solution 1