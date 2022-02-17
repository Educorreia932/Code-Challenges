import Data.List ( sort )
import System.Random ( randomRIO )
import Control.Monad ( replicateM, replicateM_ )

main :: IO ()
main = replicateM_ 6 $ replicateM 4 (randomRIO (1,6::Int)) >>= \x -> print $ sum $ drop 1 $ sort x
