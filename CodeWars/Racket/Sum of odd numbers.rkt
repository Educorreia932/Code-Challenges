#lang racket

(provide row-sum-odd-numbers)

(define (row-sum-odd-numbers n)
    (define start (- (* n n) (- n 1)))
    (apply + (build-list n (lambda (x) (+ start (* 2 x)))))
)
