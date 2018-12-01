#lang racket

(let ([data (file->list "input.txt")])
  (println (apply + data))
  (println (for/fold ([seen (set)]
                      [freq 0]
                      #:result freq)
                     ([num (in-cycle data)]
                      #:break (set-member? seen freq))
             (let ([next (+ freq num)])
               (values (set-add seen freq) next)))))
