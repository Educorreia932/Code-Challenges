module Century where

century :: Int -> Int
century year = ceiling $ fromIntegral year / 100 
