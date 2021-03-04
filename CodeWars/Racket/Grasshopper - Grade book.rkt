#lang racket

(provide get-grade)

(define (get-grade s1 s2 s3)
    (define score (/ (+ (+ s1 s2) s3) 3))
    (cond
        [(and (<= 90 score) (>= 100 score)) "A"]
        [(and (<= 80 score) (> 90 score)) "B"]
        [(and (<= 70 score) (> 80 score)) "C"]
        [(and (<= 60 score) (> 70 score)) "D"]
        [(and (<= 0 score) (> 60 score)) "F"]
    )
)
