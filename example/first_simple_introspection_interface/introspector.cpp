typedef int an_integer_is_also_a_basic_type_a_grounding;
typedef an_integer_is_also_a_basic_type_a_grounding this_is_a_type;
typedef this_is_a_type this_is_another_typedef_body;
typedef this_is_another_typedef_body this_is_a_typedef_body;
typedef this_is_a_typedef_body this_is_a_int_typename;
this_is_a_int_typename this_is_a_variable_whos_type_is_quote_this_is_a_type_name_endquote; //keep the name abstract?_it_is_a_long_chain_of_typedefs_ending_in_an_int;
 
this_is_a_int_typename & this_is_a_reference_to_another_variable=this_is_a_variable_whos_type_is_quote_this_is_a_type_name_endquote;

namespace gcc {
  typedef int size_t;
  struct string {
    void print() {};
  };
  namespace program {    
    namespace variables {
      struct variable {
        struct variable_decl {
          string name;
        };
        variable_decl decl ;
      };

      struct list_base {
        size_t size(){ return 1; };
        bool isempty() { return false; }
      };

      struct list : public list_base {
        bool isempty() {}
        size_t size() {
          if (isempty()) { return 0; }
        }

        //template <class template_list>
        struct iterator {
          list_base & source;
          //          iterator ( ) {};
          iterator (list_base  & l):source(l) 
          { };
          iterator operator ++ (int) {
          }
          bool operator < (iterator &) {
            if (source.isempty())
              {
                return 0;
              }        
          }

          bool operator < (iterator ) {
            if (source.isempty())
              {
                return 0;
              }        
          }
          variable * operator -> () {}
        };
        
        //typedef typename iterator<typename template_list> template_list_iterator_t;
        
        iterator  end() {
          
        }
          
        
      };
    };
  };
  program::variables::list list_of_variables_in_program;
};

this_is_a_int_typename this_is_what_the_program_does (int argc, char ** argv )
{
 
  gcc::list_of_variables_in_program;
  gcc::program::variables::list v;
  for (gcc::program::variables::list::iterator y=v;y<v.end();y++)    {
    y->decl.name.print();
  }


  for (gcc::program::variables::list::iterator y=v;y<v.end();y++)    {
    y->decl.name.print();
  }

  bool really_simple_return=false;

  if (really_simple_return)
    return 1 + 2 + 3 + 4 ; // ten! the world. 
  /**
     operating system interface
     rules and regulations
     automatic proving of algorithms
     proof engine
     proof
     lemma
     theorm
     definition
     the c language
     the unix operating system
     the filesystem
     device drivers
     network drivers
     function pointers
     callback functions from the operating system
     process invocation
   */

  return 0;
}

this_is_a_int_typename main (int argc, char ** argv )
{
  this_is_a_int_typename this_is_the_return_from_main = this_is_what_the_program_does(argc,argv);

  return this_is_the_return_from_main;
}



