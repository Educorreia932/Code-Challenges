areaOrPerimeter :: Double -> Double -> Double
areaOrPerimeter l w | l == w = l * w
                    | otherwise = l * 2 + w * 2