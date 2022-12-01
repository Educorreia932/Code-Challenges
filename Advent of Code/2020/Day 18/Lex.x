{
module Lex where
}

%wrapper "basic"

$digit = [0-9]

tokens :-

$white+ ;
"+"     {\_ -> Plus}
"*"     {\_ -> Times}
"("     {\_ -> LP}
")"     {\_ -> RP}
$digit+ {\x -> N (read x)}

{
data Token = Plus | Times | LP | RP | N Int 
}