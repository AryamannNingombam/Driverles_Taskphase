; Auto-generated. Do not edit!


(cl:in-package task_2-msg)


;//! \htmlinclude eligibility.msg.html

(cl:defclass <eligibility> (roslisp-msg-protocol:ros-message)
  ((person
    :reader person
    :initarg :person
    :type task_2-msg:nameAge
    :initform (cl:make-instance 'task_2-msg:nameAge))
   (eligi
    :reader eligi
    :initarg :eligi
    :type cl:string
    :initform ""))
)

(cl:defclass eligibility (<eligibility>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <eligibility>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'eligibility)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name task_2-msg:<eligibility> is deprecated: use task_2-msg:eligibility instead.")))

(cl:ensure-generic-function 'person-val :lambda-list '(m))
(cl:defmethod person-val ((m <eligibility>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader task_2-msg:person-val is deprecated.  Use task_2-msg:person instead.")
  (person m))

(cl:ensure-generic-function 'eligi-val :lambda-list '(m))
(cl:defmethod eligi-val ((m <eligibility>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader task_2-msg:eligi-val is deprecated.  Use task_2-msg:eligi instead.")
  (eligi m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <eligibility>) ostream)
  "Serializes a message object of type '<eligibility>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'person) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'eligi))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'eligi))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <eligibility>) istream)
  "Deserializes a message object of type '<eligibility>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'person) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'eligi) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'eligi) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<eligibility>)))
  "Returns string type for a message object of type '<eligibility>"
  "task_2/eligibility")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'eligibility)))
  "Returns string type for a message object of type 'eligibility"
  "task_2/eligibility")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<eligibility>)))
  "Returns md5sum for a message object of type '<eligibility>"
  "605e2e8c6dcc5e2732ee00e0daddc6e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'eligibility)))
  "Returns md5sum for a message object of type 'eligibility"
  "605e2e8c6dcc5e2732ee00e0daddc6e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<eligibility>)))
  "Returns full string definition for message of type '<eligibility>"
  (cl:format cl:nil "nameAge person~%string eligi~%================================================================================~%MSG: task_2/nameAge~%string name~%int64 age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'eligibility)))
  "Returns full string definition for message of type 'eligibility"
  (cl:format cl:nil "nameAge person~%string eligi~%================================================================================~%MSG: task_2/nameAge~%string name~%int64 age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <eligibility>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'person))
     4 (cl:length (cl:slot-value msg 'eligi))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <eligibility>))
  "Converts a ROS message object to a list"
  (cl:list 'eligibility
    (cl:cons ':person (person msg))
    (cl:cons ':eligi (eligi msg))
))
