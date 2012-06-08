/*
 * Subject to the GPL, v.2
 */
using namespace std;
#include <gold/gold.h>

#include <cstring>
#include <list>
//#include <string>
//#include <iostream>
//#include <fstream>
#include <utility>
#include <set>
//#include <map>
#include <vector>
#include <algorithm>

#include <gold/symtab.h>
#include <gold/object.h>
#include <gold/parameters.h>
#include <gold/errors.h>
#include <gold/options.h>
#include <gold/binary.h>


#include <elfcpp/elfcpp.h>
#include <elfcpp/elfcpp_file.h>

#include <libelf.h>
  // open http://pubs.opengroup.org/onlinepubs/000095399/functions/open.html
#include <sys/stat.h>
#include <sys/fcntl.h>
  // from http://www.vbforums.com/showthread.php?t=556042

#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


int main (int argc, char ** argv )
{
  gold::parameters_clear_target();

    //    gold::Object::View v (hdr);
    //    elfcpp::Elf_file<64, false, gold::Object> test(&v);

    //    Dirsearch* dirpath
      
    /*      Input_file_argument input_file_arg(member_name->c_str(),
			      Input_file_argument::INPUT_FILE_TYPE_FILE,
			      "", false, parameters->options());
    Input_file input_file(input_file_arg);
    */
    //    *input_file = new Input_file("/proc/self/exe");
    const gold::Task* task = reinterpret_cast<const gold::Task*>(-1);

    struct stat st;
    const char * program_name="/proc/self/exe";
    gold::Errors errors(program_name);
    gold::set_parameters_errors(&errors);

    gold::General_options options;
    gold::set_parameters_options(&options);

    ::stat(program_name, &st);
    int o = ::open(program_name, O_RDONLY);
    unsigned char* filedata = new unsigned char[st.st_size];
    size_t readc= ::read(o, filedata, st.st_size) ;
    ::close(o);

    gold::Binary_to_elf binary(static_cast<elfcpp::EM>(0xffff), 64, 0,
			 program_name);


    gold::Input_file input_file(task, program_name, binary.converted_data(),
			binary.converted_size());

   
    gold::Object* object = make_elf_object(program_name, &input_file, 0,
				   binary.converted_data(),
				   binary.converted_size(), NULL);

    //    gold::Object obj(string("thisprogram",input_file, false,0);

  return 0;
}



