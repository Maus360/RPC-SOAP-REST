namespace py tutorial

/*
 C like comments are supported
*/
// This is also a valid comment

typedef i32 int // We can use typedef to get pretty names for the types we are using

struct ThType{
        1: string name,
        2: string min,
        3: string max,
        4: string format,
        5: int size,
        6: string description
        7: int id
}

struct ThMathOperation{
        1: string name,
        2: string type_of_argument,
        3: string type_of_value,
        4: string description,
        5: int id
}

struct ThClass{
        1: string name,
        2: int number_of_methods,
        3: int number_of_properties,
        4: int id
}

exception InvalidID {
  1: i32 id,
  2: string why
}

service MyService
{
        list<ThClass> get_class_all()
        ThClass get_class(1:int id),
        void set_class(1: string name, 2: int number_of_methods, 3: int number_of_properties)
        void reset_class(1: int id, 2:string name, 3: int number_of_methods, 4: int number_of_properties)
        void delete_class(1: int id)

        list<ThMathOperation> get_math_operations_all()
        ThMathOperation get_math_peration(1:int id),
        void set_math_operation(1: string name, 2: string type_of_argument, 3: string type_of_value, 4: string description)
        void reset_math_operation(1: int id, 2: string name, 3: string type_of_argument, 4: string type_of_value, 5: string description)
        void delete_math_operation(1: int id)

        list<ThType> get_type_all()
        ThType get_type(1:int id),
        void set_type(1: string name, 2: string min,3: string max, 4: string format, 5: int size, 6: string description)
        void reset_type(1: int id, 2: string name, 3: string min, 4: string max, 5: string format, 6: int size, 7: string description)
        void delete_type(1: int id)

}