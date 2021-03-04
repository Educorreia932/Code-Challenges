#lang racket

(provide final-grade)

(define (final-grade exam projects)
    (cond
        [(or (> exam 90) (> projects 10)) 100]
        [(and (> exam 75) (>= projects 5)) 90]
        [(and (> exam 50) (>= projects 2)) 75]
        [else 0] 
    )
)
