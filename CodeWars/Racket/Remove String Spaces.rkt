#lang racket

(provide remove-spaces)

(define (remove-spaces str)
    (string-replace str " " "")
)
