
(cl:in-package :asdf)

(defsystem "task_2-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "nameAge" :depends-on ("_package_nameAge"))
    (:file "_package_nameAge" :depends-on ("_package"))
  ))