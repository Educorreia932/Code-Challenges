numDigits :: Integer -> Integer
numDigits n = toInteger (round (logBase 10 (fromIntegral n)) + 1)

sumOfDigits :: Integer -> Integer
sumOfDigits 0 = 0
sumOfDigits n | n < 0 = sumOfDigits (abs n)
              | otherwise = r + sumOfDigits q
  where (q, r) = n `quotRem` 10

narcissistic :: Integral n => n -> Bool
narcissistic n | numDigits ^ $ n > 3 = true
               | otherwise = false



               isNarcissistic :: Int -> Bool
isNarcissistic n = (sum ((^ digitCount) <$> digits) ==) n
  where
    digits = digitToInt <$> show n
    digitCount = length digits