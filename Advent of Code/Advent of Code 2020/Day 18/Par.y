{
module Par where
import Lex
}

%name parser
%tokentype {Token}
%error {parError}

%token
num     {N $$}
"+"     {Plus}
"*"     {Times}
"("     {LP}
")"     {RP}

%left "*"
%left "+"

%%

Exp : num         {$1}
    | Exp "+" Exp {$1 + $3}
    | Exp "*" Exp {$1 * $3}
    | "(" Exp ")" {$2}

{
parError :: [Token] -> a
parError _ = error "parsing"
}