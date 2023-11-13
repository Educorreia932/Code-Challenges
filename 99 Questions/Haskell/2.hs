myButLast :: [a] -> a
myButLast [] = error "Empty list"
myButLast [x] = error "List too short"
myButLast [x,_] = x
myButLast (_:xs) = myButLast xs
