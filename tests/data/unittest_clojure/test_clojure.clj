;@start()
;Starting
;--------

;comments: with indentation
;@include(comments)

;    @include(comments)


;Code included:
;==============
;@include(test_area)
;@

;@start(comments)
;		comment line 1
;		comment line 2
;@(comments)


; @cstart(test_area) 
(defn hello-world [] (println "Hello, World!"))
; @(test_area)