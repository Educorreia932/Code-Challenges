#lang racket

(provide find-smallest-int)

(define (find-smallest-int lst)
    (define (min x1 x2)
        (if (< x1 x2) x1 x2))
    (foldl min (first lst) (rest lst))
)   
