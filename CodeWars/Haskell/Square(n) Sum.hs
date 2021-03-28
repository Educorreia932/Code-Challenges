module SquareSum where

squareSum :: [Integer] -> Integer
squareSum numbers = sum $ map (^2) numbers 