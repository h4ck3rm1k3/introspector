/*
 * Subject to the GPL, v.2
 */

typedef int an_integer_is_also_a_basic_type_a_grounding;
typedef an_integer_is_also_a_basic_type_a_grounding this_is_a_type;
typedef this_is_a_type this_is_another_typedef_body;
typedef this_is_another_typedef_body this_is_a_typedef_body;
typedef this_is_a_typedef_body this_is_a_int_typename;
this_is_a_int_typename this_is_a_variable_whos_type_is_quote_this_is_a_type_name_endquote; //keep the name abstract?_it_is_a_long_chain_of_typedefs_ending_in_an_int;
 
this_is_a_int_typename & this_is_a_reference_to_another_variable=this_is_a_variable_whos_type_is_quote_this_is_a_type_name_endquote;

#include "gettext.h"
#include <cstring>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <utility>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

#include <elfcpp/elfcpp.h>
#include <elfcpp/elfcpp_file.h>

#include <libelf.h>
  // open http://pubs.opengroup.org/onlinepubs/000095399/functions/open.html
#include <sys/stat.h>
#include <sys/fcntl.h>
  // from http://www.vbforums.com/showthread.php?t=556042

using namespace std;

namespace libelf {
 
  void readType(Elf64_Ehdr * hdr) {
    // from http://www.hep.wisc.edu/~pinghc/Detect_the_file_type.htm
    if(hdr!=NULL) 
      {
	switch(hdr->e_type)
	  {
	  case 1:
	    cout<<"File Tyep: ET_REL 1 /* Relocatable file */"<<endl;
	    break;
	  case 2:
	    cout<<"File TYpe: ET_EXEC 2 /* Executable file */"<<endl;
	    break;
	  default:
	    cout<<"File Type: else types"<<endl;
	  }
	
	switch(hdr->e_machine)
	  {
	  case 0:
	    cout<<"Machine type: EM_NONE	0 /* No machine */"<<endl;
	    break;
	  case 1:
	    cout<<"Machine type: EM_M32 1 /* AT&T WE 32100 */"<<endl;
	    break;
	  case 2:
	    cout<<"Machine type: EM_SPARC 2 /* SUN SPARC */"<<endl;
	    break;
	  case 3:
	    cout<<"Machine type: EM_386 3 /* Intel 80386 */"<<endl;
	    break;
	  default:
	    cout<<"else types"<<endl;
	  }
      }
    else
      cout<<"hdr ptr points to NULL"<<endl;
  }
  
  // from linux kernel linux/linux/arch/x86/vdso/vma.c
  
  void check_vdso64(Elf64_Ehdr *hdr)
  {
    Elf64_Shdr *sechdrs, *alt_sec = 0;
    char *secstrings;
    int i;
    
    cout << "Check hdr " << hdr << "\n";
    cout << "Check hdr e_shoff " << hdr->e_shoff << "\n";

    Elf64_Shdr *  shdr0 = (Elf64_Shdr *) (hdr->e_shoff + (void*)hdr);
    cout << "Check hdr + e_shoff " << shdr0 << "\n";
    cout << "Check  hdr->e_shstrndx " << hdr->e_shstrndx << "\n";

    // crash cout << "check" << hdr + shdr0[0].sh_offset;
   
    // const char * name_table = (const char *) hdr + shdr0[hdr->e_shstrndx].sh_offset;
    //cout << "Check  name_table " << name_table << "\n";


    //Elf_Shdr const *const symsec = &shdr0[symsec_sh_link];
    //    Elf_Shdr const *const strsec = &shdr0[w(symsec->sh_link)];

    //segfault    secstrings = (char *)(hdr + sechdrs[hdr->e_shstrndx].sh_offset);
    //cout << "Check hdr secstrings " << secstrings << "\t";

    for (i = 1; i < hdr->e_shnum; i++) {
      //Elf64_Shdr *shdr = &sechdrs[i];
      //cout << "Check vdo " << secstrings + shdr->sh_name << "\t";
      //alt_sec = shdr;
      //cout << hdr + shdr->sh_offset << "\t";
      //      cout << alt_sec->sh_size << endl;
      
    }
  }
  
  bool readelf() {
    cout << "reading elf!" << endl;
    int fileDescriptor = open("/proc/self/exe", O_RDONLY); 

    elf_version(EV_CURRENT);

    Elf *elf = elf_begin(fileDescriptor, ELF_C_READ, NULL);
    cout << "read elf" << elf << endl;

    Elf64_Ehdr *header = 0; // ELF Header
    Elf_Scn *section = 0; // ELF Section
    Elf_Data *sectionData = 0; // ELF Section Data
    Elf64_Shdr *sectionHeader = 0; // ELF Section Header
    int symbolNumber = -1;
    if(!elf) { 
      cerr << "elf begin failed!" << endl;
      goto end; 
    }
    else {
      cerr << "elf" << elf << endl;
    }

    unsigned short ndx;
    if((header = elf64_getehdr(elf)) == 0) {
      cerr << "cannot get header!" << endl;
      goto error;
      //elf_end(elf);
      //close(fileDescriptor);
      //return false;
    }

    cout << "check_vdso64" << endl;
    check_vdso64(header); // another function
    readType(header); // another function

    ndx = header->e_shstrndx;
    // Go through the sections
    // .dynsym = Dynamic Symbol Location (linked with .hash and .dynstr)
    while((section = elf_nextscn(elf, section)) != 0) {

      if((sectionHeader = elf64_getshdr(section)) != 0) {
	string name = elf_strptr(elf, ndx, (size_t)sectionHeader->sh_name);
	cout << "section name :" << name << endl;


	// 
	if(name != ".dynsym") {
	  Elf64_Shdr *strtabhdr;
	  Elf64_Sym *symbol, *symbolp; // ELF Symbol Pointers
	  char *astring;
	  strtabhdr = &sectionHeader[sectionHeader->sh_link];
	  astring = (char *)malloc(strtabhdr->sh_size);
	  if(astring == NULL) goto error;
	  if((size_t)lseek(fileDescriptor, strtabhdr->sh_offset, SEEK_SET) != strtabhdr->sh_offset) goto error;
	  if((size_t)read(fileDescriptor, astring, strtabhdr->sh_size) != strtabhdr->sh_size) goto error;
	  symbol = (Elf64_Sym *)malloc(sectionHeader->sh_size);
	  if(symbol == NULL) goto error;
	  if((size_t)lseek(fileDescriptor, sectionHeader->sh_offset, SEEK_SET) != sectionHeader->sh_offset) goto error;
	  if((size_t)read(fileDescriptor, symbol, sectionHeader->sh_size) != sectionHeader->sh_size) goto error;

	  symbolp = symbol;
	  for(int i = 0; (size_t)i < sectionHeader->sh_size; i += sizeof(Elf64_Sym)) 
	    {
	      const char * s=elf_strptr(elf, sectionHeader->sh_link, symbolp->st_name);
	      if (s){
		string name(s);	      
		cout << name << "\t"<< i << endl;
	      }
	      else
		{
		  cout << "NULL name" << "\t"<< i << endl;
		}
	      ++symbolp;
	    }

	} // dynsym

	} else continue;

    }
    // .rel.plt = Relocation Procedure Linkage Table (Actual GOT)
    if(symbolNumber == -1) goto error;
    // Lookup the Hash from .dynsym in .rel.plt
    section = 0; sectionHeader = 0;
    while((section = elf_nextscn(elf, section)) != 0) {
      char *name = 0;
      if((sectionHeader = elf64_getshdr(section)) != 0) {
	name = elf_strptr(elf, ndx, (size_t)sectionHeader->sh_name);

	cout << "section name :" << name << endl;

	//help #	if(!strcmp(name, ".rel.plt")) 
	{
	  sectionData = elf_getdata(section, NULL);
	  if(!sectionData) goto error;
	  for(int i = 0; (size_t)i < (sectionHeader->sh_size / sectionHeader->sh_entsize); i++) {
	    //GElf_Rel relocation;
	    //gelf_getrel(sectionData, i, &relocation);
	    //	    if(ELF64_R_SYM(relocation.r_info) == (size_t)symbolNumber) {

	    cout <<  sectionHeader->sh_name << endl;
	    //	    cout <<  sectionHeader.sh_type << endl;
	    //cout <<  sectionHeader.sh_flags << endl;

	      }
	    }
	  }


    }
  end:
    close(fileDescriptor);
    elf_end(elf);
    return true;
  error:
    close(fileDescriptor);
    elf_end(elf);
    return false;
  }
  
};

namespace gcc {
  //  typedef int size_t;
  /*
  struct string {
    void print() {};
    };*/

  namespace program {    

    extern const char filename[] = __FILE__;


    void print_current_process_T(const char * Str) 
    {
      string S(Str);
      S= "/proc/self/" + S;
      ifstream inf(S);
      cout << "Starting:"<< S << endl;
      int ch = inf.get();
      while (inf.good()) {
	cout << (char) ch;
	ch = inf.get();
      }
    }

    void print_current_process_all() {
      libelf::readelf();
      // this is a dir      print_current_process_T("cwd");
      //print_current_process_T("exe");
      print_current_process_T("env");
      print_current_process_T("mem");
      print_current_process_T("status");
      print_current_process_T("cmdline");
      
    }

    namespace variables {
      struct variable {
        struct variable_decl {
	  string name;
	  void print() {
	    cout << name  << endl;
	}
        };
        variable_decl decl ;
	void print() {
	  decl.print();
	}
      };
      
      typedef list<variable> t_variable_list;
      t_variable_list list;
      
    };
  };
};


void run_client_introspection () {

  cout << "welcome to the introspector!" << endl;
  gcc::program::print_current_process_all();

  for (
       gcc::program::variables::t_variable_list::iterator y=gcc::program::variables::list.begin();
       y != gcc::program::variables::list.end();
       y++)    {
    y->decl.print();
  }
}

this_is_a_int_typename this_is_what_the_program_does (int argc, char ** argv )
{
  run_client_introspection();
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



