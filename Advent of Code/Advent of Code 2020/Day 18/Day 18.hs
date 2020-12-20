import Lex
import Par

main = do
    interact $ unlines . (\x -> [x]) . show . sum . map (parser . alexScanTokens) . lines