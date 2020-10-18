isPrime :: Integer -> Bool
isPrime 1 = False
isPrime 2 = True
isPrime n | n <= 0 = False
          | (length [x | x <- [2 .. floor $ sqrt $ fromIntegral n], n `mod` x == 0]) > 0 = False
          | otherwise = True