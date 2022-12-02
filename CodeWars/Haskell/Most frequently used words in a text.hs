import Data.List
import Data.Function (on)
import Data.Text (toLower, pack, unpack)

top3 :: [Char] -> [[Char]]
top3 s = take 3 $ map head $ sortBy (flip compare `on` length) . group . sort $ words $ filter (flip notElem "#\\/,.") $ unpack . toLower . pack s

main = do
    print $ top3 "aa a aa aaa b"