#lang racket

(provide sum)

(define (sum lst)
    (foldr + 0 lst)
)
