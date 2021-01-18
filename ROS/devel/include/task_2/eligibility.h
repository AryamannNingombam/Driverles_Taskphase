// Generated by gencpp from file task_2/eligibility.msg
// DO NOT EDIT!


#ifndef TASK_2_MESSAGE_ELIGIBILITY_H
#define TASK_2_MESSAGE_ELIGIBILITY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <task_2/nameAge.h>

namespace task_2
{
template <class ContainerAllocator>
struct eligibility_
{
  typedef eligibility_<ContainerAllocator> Type;

  eligibility_()
    : person()
    , eligi()  {
    }
  eligibility_(const ContainerAllocator& _alloc)
    : person(_alloc)
    , eligi(_alloc)  {
  (void)_alloc;
    }



   typedef  ::task_2::nameAge_<ContainerAllocator>  _person_type;
  _person_type person;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _eligi_type;
  _eligi_type eligi;





  typedef boost::shared_ptr< ::task_2::eligibility_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::task_2::eligibility_<ContainerAllocator> const> ConstPtr;

}; // struct eligibility_

typedef ::task_2::eligibility_<std::allocator<void> > eligibility;

typedef boost::shared_ptr< ::task_2::eligibility > eligibilityPtr;
typedef boost::shared_ptr< ::task_2::eligibility const> eligibilityConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::task_2::eligibility_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::task_2::eligibility_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::task_2::eligibility_<ContainerAllocator1> & lhs, const ::task_2::eligibility_<ContainerAllocator2> & rhs)
{
  return lhs.person == rhs.person &&
    lhs.eligi == rhs.eligi;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::task_2::eligibility_<ContainerAllocator1> & lhs, const ::task_2::eligibility_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace task_2

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::task_2::eligibility_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::task_2::eligibility_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::task_2::eligibility_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::task_2::eligibility_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::task_2::eligibility_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::task_2::eligibility_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::task_2::eligibility_<ContainerAllocator> >
{
  static const char* value()
  {
    return "605e2e8c6dcc5e2732ee00e0daddc6e4";
  }

  static const char* value(const ::task_2::eligibility_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x605e2e8c6dcc5e27ULL;
  static const uint64_t static_value2 = 0x32ee00e0daddc6e4ULL;
};

template<class ContainerAllocator>
struct DataType< ::task_2::eligibility_<ContainerAllocator> >
{
  static const char* value()
  {
    return "task_2/eligibility";
  }

  static const char* value(const ::task_2::eligibility_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::task_2::eligibility_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nameAge person\n"
"string eligi\n"
"================================================================================\n"
"MSG: task_2/nameAge\n"
"string name\n"
"int64 age\n"
;
  }

  static const char* value(const ::task_2::eligibility_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::task_2::eligibility_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.person);
      stream.next(m.eligi);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct eligibility_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::task_2::eligibility_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::task_2::eligibility_<ContainerAllocator>& v)
  {
    s << indent << "person: ";
    s << std::endl;
    Printer< ::task_2::nameAge_<ContainerAllocator> >::stream(s, indent + "  ", v.person);
    s << indent << "eligi: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.eligi);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TASK_2_MESSAGE_ELIGIBILITY_H
