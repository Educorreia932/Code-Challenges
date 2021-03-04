#lang racket

(provide enough)

(define (enough cap on wait)
    (define board (- wait (- cap on)))
    (if (> board 0) board 0)
)
