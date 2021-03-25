#lang racket
(provide new-avg)

(define (new-avg ls navg)
    (define l (+ (length ls) 1))
    (define s (apply + ls))
    (define result (exact-ceiling (- (* l navg) s)))
    (if (positive? result) result (raise-argument-error 'Negative result "negative?" result))
)
