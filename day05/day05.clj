(ns advent-2018.day-5
  (:require [clojure.string :as str]))

(def input (str/trim (slurp "input.txt")))

(defn reacts? [l r] (= 32 (Math/abs (- (int l) (int r)))))

(defn add-unit [res c]
  (if (some-> (peek res) (reacts c))
    (pop res) (conj res c)))

(defn react [in] (reduce add-unit [] in))

(count (react input))

(defn remove-units [x polymer]
  (remove (fn [y] (or (= x y) (reacts? x y))) polymer))

(->> (map char (range 97 123))
     (map #(count (react (remove-units % input))))
     (apply min))
