#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#define MSG "hello"
#define N 5

int
writefile(char *dirname, char *filename)
{
	int    fildes;
	char   oldcwd[FILENAME_MAX];
	getcwd(oldcwd, FILENAME_MAX / (sizeof (char)));
	if (chdir(dirname) == 0) {
		fildes = open(filename, O_WRONLY|O_CREAT|O_CLOEXEC, 0644);
		if (fildes == -1) {
			printf("Failed to open %s file.\n", filename);
			chdir(oldcwd);
			return 1;
		}
		if (write(fildes, MSG, N) != N) {
			printf("Failed to write %s in %s", MSG, filename);
			chdir(oldcwd);
			return 1;
		}
		chdir(oldcwd);
		return 0;
	} else {
		printf("Directory %s does not exist.\n", dirname);
		chdir(oldcwd);
		return 1;
	}
}

int
main(void)
{
	writefile("/tmp/f1", "file1.txt");
	writefile("/tmp/f2", "file2.txt");
	writefile("/tmp/f3", "file3.txt");
	writefile("/tmp/f4", "file4.txt");
	writefile("/tmp/f5", "file5.txt");
	writefile("/tmp/f6", "file6.txt");
	writefile("/tmp/f7", "file7.txt");
	writefile("/tmp/f8", "file8.txt");
	return 0;
}
