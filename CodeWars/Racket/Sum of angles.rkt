#lang racket

(provide angle)

(define (angle n)
    (- (* 180 n) 360)
)
