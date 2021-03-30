module RemoveExclamationMarks where

removeExclamationMarks :: String -> String
removeExclamationMarks = filter (/= '!')
