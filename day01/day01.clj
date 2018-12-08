(ns advent-2018.day-1
  (:require [clojure.string :as str]))

(def input (->> (slurp "input.txt")
               str/split-lines
               (map read-string)))
(reduce + input)
(reduce (fn [seen acc]
          (if (contains? seen acc)
            (reduced acc)
            (conj seen acc)))
        #{} (reductions + (cycle input)))
