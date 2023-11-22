data Encoding a = Multiple Int a | Single a deriving (Show)

encodeModified :: (Eq a) => [a] -> [Encoding a]
encodeModified [] = []
encodeModified list = encoding : encodeModified rest
  where
    (start, rest) = span (== head list) list
    encoding = case length start of
        1 -> Single (head start)
        _ -> Multiple (length start) (head start)