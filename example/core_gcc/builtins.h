//

void gcc_built_in_type_int(int x) {
  char description[]="The int is a basic type";
}

void parameter_range(void *parameter,const void * value, const char * descr){
  char description[]="We define that this parameter has this possible value in the range and the description descr";  
}

const int	EXIT_FAILURE=	1;
const int 	EXIT_SUCCESS=	0;

void _exit( int status);

void describe__exit(int status) {
  void * function = _exit;
  const char header[] = "unistd.h";
  parameter_range(&status,&EXIT_FAILURE,"Failing exit status.");
  parameter_range(&status,&EXIT_SUCCESS,"Successful exit status");
}
