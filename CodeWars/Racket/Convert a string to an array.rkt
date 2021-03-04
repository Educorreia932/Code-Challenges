#lang racket

(provide string-to-vector)

(define (string-to-vector string)
    (list->vector (string-split string (regexp "[ ]+")))
)
