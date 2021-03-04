#lang racket

(provide factor?)

(define (factor? base factor)
    (= (modulo base factor) 0)
)
