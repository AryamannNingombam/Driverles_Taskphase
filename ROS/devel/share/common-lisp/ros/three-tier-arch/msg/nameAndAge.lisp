; Auto-generated. Do not edit!


(cl:in-package three-tier-arch-msg)


;//! \htmlinclude nameAndAge.msg.html

(cl:defclass <nameAndAge> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (age
    :reader age
    :initarg :age
    :type cl:fixnum
    :initform 0))
)

(cl:defclass nameAndAge (<nameAndAge>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <nameAndAge>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'nameAndAge)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name three-tier-arch-msg:<nameAndAge> is deprecated: use three-tier-arch-msg:nameAndAge instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <nameAndAge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader three-tier-arch-msg:name-val is deprecated.  Use three-tier-arch-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'age-val :lambda-list '(m))
(cl:defmethod age-val ((m <nameAndAge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader three-tier-arch-msg:age-val is deprecated.  Use three-tier-arch-msg:age instead.")
  (age m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <nameAndAge>) ostream)
  "Serializes a message object of type '<nameAndAge>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'age)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <nameAndAge>) istream)
  "Deserializes a message object of type '<nameAndAge>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'age)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<nameAndAge>)))
  "Returns string type for a message object of type '<nameAndAge>"
  "three-tier-arch/nameAndAge")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'nameAndAge)))
  "Returns string type for a message object of type 'nameAndAge"
  "three-tier-arch/nameAndAge")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<nameAndAge>)))
  "Returns md5sum for a message object of type '<nameAndAge>"
  "453db5a1253432b9f9c5ecabc5695077")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'nameAndAge)))
  "Returns md5sum for a message object of type 'nameAndAge"
  "453db5a1253432b9f9c5ecabc5695077")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<nameAndAge>)))
  "Returns full string definition for message of type '<nameAndAge>"
  (cl:format cl:nil "string name~%uint8 age ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'nameAndAge)))
  "Returns full string definition for message of type 'nameAndAge"
  (cl:format cl:nil "string name~%uint8 age ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <nameAndAge>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <nameAndAge>))
  "Converts a ROS message object to a list"
  (cl:list 'nameAndAge
    (cl:cons ':name (name msg))
    (cl:cons ':age (age msg))
))
