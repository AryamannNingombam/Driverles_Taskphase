;; Auto-generated. Do not edit!


(when (boundp 'task_2::eligibility)
  (if (not (find-package "TASK_2"))
    (make-package "TASK_2"))
  (shadow 'eligibility (find-package "TASK_2")))
(unless (find-package "TASK_2::ELIGIBILITY")
  (make-package "TASK_2::ELIGIBILITY"))

(in-package "ROS")
;;//! \htmlinclude eligibility.msg.html


(defclass task_2::eligibility
  :super ros::object
  :slots (_person _eligi ))

(defmethod task_2::eligibility
  (:init
   (&key
    ((:person __person) (instance task_2::nameAge :init))
    ((:eligi __eligi) "")
    )
   (send-super :init)
   (setq _person __person)
   (setq _eligi (string __eligi))
   self)
  (:person
   (&rest __person)
   (if (keywordp (car __person))
       (send* _person __person)
     (progn
       (if __person (setq _person (car __person)))
       _person)))
  (:eligi
   (&optional __eligi)
   (if __eligi (setq _eligi __eligi)) _eligi)
  (:serialization-length
   ()
   (+
    ;; task_2/nameAge _person
    (send _person :serialization-length)
    ;; string _eligi
    4 (length _eligi)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; task_2/nameAge _person
       (send _person :serialize s)
     ;; string _eligi
       (write-long (length _eligi) s) (princ _eligi s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; task_2/nameAge _person
     (send _person :deserialize buf ptr-) (incf ptr- (send _person :serialization-length))
   ;; string _eligi
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _eligi (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get task_2::eligibility :md5sum-) "605e2e8c6dcc5e2732ee00e0daddc6e4")
(setf (get task_2::eligibility :datatype-) "task_2/eligibility")
(setf (get task_2::eligibility :definition-)
      "nameAge person
string eligi
================================================================================
MSG: task_2/nameAge
string name
int64 age

")



(provide :task_2/eligibility "605e2e8c6dcc5e2732ee00e0daddc6e4")


