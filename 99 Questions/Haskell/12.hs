data Encoding a = Multiple Int a | Single a deriving (Show)

decodeModified :: (Eq a) => [Encoding a] -> [a]
decodeModified [] = []
decodeModified (x:xs) = decoded ++ decodeModified xs
    where 
        decoded = case x of 
            Multiple i a -> replicate i a
            Single a -> [a]