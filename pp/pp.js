int *ptr; // Declares a pointer to an integer
int num = 10;
int *ptr = &num; // Assigns the address of 'num' to 'ptr'
int value = *ptr; // Retrieves the value at the address stored in 'ptr' (in this case, the value of 'num')
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr; // 'ptr' points to the first element of 'arr'

printf("%d\n", *ptr); // Prints the value at the first element (prints '1')
ptr++; // Moves 'ptr' to the next element in the array
printf("%d\n", *ptr); // Prints the value at the second element (prints '2')
