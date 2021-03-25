#lang racket
(provide potatoes)

(define (potatoes p0 w0 p1)
    (define _p0 (/ p0 100))
    (define _p1 (/ p1 100))
    (exact-floor (/ (* (- 1 _p0) w0) (- 1 _p1)))
)
