#lang racket

(provide litres)

(define (litres time)
    (exact-floor (/ time 2))
)
