;; Auto-generated. Do not edit!


(when (boundp 'task_2::nameAge)
  (if (not (find-package "TASK_2"))
    (make-package "TASK_2"))
  (shadow 'nameAge (find-package "TASK_2")))
(unless (find-package "TASK_2::NAMEAGE")
  (make-package "TASK_2::NAMEAGE"))

(in-package "ROS")
;;//! \htmlinclude nameAge.msg.html


(defclass task_2::nameAge
  :super ros::object
  :slots (_name _age ))

(defmethod task_2::nameAge
  (:init
   (&key
    ((:name __name) "")
    ((:age __age) 0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _age (round __age))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:age
   (&optional __age)
   (if __age (setq _age __age)) _age)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; uint8 _age
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; uint8 _age
       (write-byte _age s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _age
     (setq _age (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get task_2::nameAge :md5sum-) "453db5a1253432b9f9c5ecabc5695077")
(setf (get task_2::nameAge :datatype-) "task_2/nameAge")
(setf (get task_2::nameAge :definition-)
      "string name
uint8 age

")



(provide :task_2/nameAge "453db5a1253432b9f9c5ecabc5695077")


