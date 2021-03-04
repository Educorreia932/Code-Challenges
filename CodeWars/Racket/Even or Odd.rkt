#lang racket

(provide even-or-odd)

(define (even-or-odd n)
    (if (even? n) "Even" "Odd")
)
