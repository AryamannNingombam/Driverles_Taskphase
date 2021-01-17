
(cl:in-package :asdf)

(defsystem "three-tier-arch-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "nameAndAge" :depends-on ("_package_nameAndAge"))
    (:file "_package_nameAndAge" :depends-on ("_package"))
  ))