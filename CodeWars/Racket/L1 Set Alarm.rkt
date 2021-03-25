#lang racket

(provide set-alarm)

(define (set-alarm employed vacation)
    (and employed (not vacation))
)
