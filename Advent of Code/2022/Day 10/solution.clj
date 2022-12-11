(require '[clojure.string :as str])
(require '[clojure.java.io :as io])


(defn part-one [instructions]
  	(let [cycles
        (flatten (map (fn [instruction]
                        	(let [arguments (str/split instruction #" ")]
                          		(case (first arguments)
                            		"noop" [0]
                            		"addx" [0, (Integer/parseInt (second arguments))])))
                      		instructions))]

    (reduce + (map (fn [i] (* (+ i 1) (+ 1 (reduce + (take i cycles))))) (range 19 221 40)))))


(defn read-input []
  	(with-open [rdr (io/reader "input.txt")]
    	(reduce conj [] (line-seq rdr))))

(def instructions (read-input))

(println (part-one instructions))
