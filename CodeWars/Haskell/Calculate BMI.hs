module BodyMassIndex where

bmi :: Float -> Float -> String  
bmi weight height | result <= 18.5 = "Underweight"
                  | result <= 25.0 = "Normal"
                  | result <= 30.0 = "Overweight"
                  | result > 30.0 = "Obese"
                  where result = weight / height ^ 2 