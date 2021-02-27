#lang racket
(require rackunit rackunit/text-ui)

(provide maps)

(define (maps lst)
    (map (lambda (n) (* 2 n)) lst)
)