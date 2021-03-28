#lang racket
(provide square-sum)

(define (square-sum numbers)
    (foldr + 0 (map (lambda (number) (expt number 2)) numbers))
)