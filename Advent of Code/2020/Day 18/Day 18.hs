import Lex
import Par

main = interact $ unlines . (\x -> [x]) . show . sum . map (parser . alexScanTokens) . lines