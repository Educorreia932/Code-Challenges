#lang racket

(provide divisors)

(define (divisors n)
    (length (filter (lambda (x) (= (remainder n x) 0)) (range 1 (+ n 1))))
)
