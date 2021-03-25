#lang racket

(provide find-needle)

(define (index lst)
    (if (string=? (first lst) "needle") 
        0
        (+ 1 (find-needle (rest lst)))
    )
) 

(define (find-needle lst)
    (format "found the needle at position ~a" (index lst))
)
