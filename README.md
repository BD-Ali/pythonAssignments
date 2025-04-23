# pythonAssignments
python 1st assignment


====Secant method function=====
first we convert the string function to a function that the compiler can read and put it in variable f.
then will initialize epsilon to value of 0.001 and the max_iter to 30 as the maximum iterations of the method that we will use.
then will iterate 30 times and apply the secant formula each time on more accurate Fx1 and Fx2 and each iteration will check.
if the function value is close to 0 will return the root (x1).
then will check if the value didn't change much will return the root (x1).
then will calculate the next value of the secant method and checks if the denominator is too small (to avoid division by zero) will stop the iteration and return it.
else will continue the iteration until we get the smallest root after 30 iterations and return it.



====Matrix Gaussian elimination=====
first we enter the matrix rows length in a variable "r" if the length is zero we return the same matrix because we have no thing to do with it.
then will enter the length of the first column in variable "c" and create a copy of the original to do the changes on it.
then we have a for loop that loops through each pivot row up to the last column before the augmented part.
then if the pivot is zero will fix it using partial pivoting.
after we search for a non-zero value below the pivot and swap rows. 
if no non zero pivot found will skip the column.
now will divide by the current pivot until its 1 as required.
and lastly will eliminate the entries below the pivot by subtracting a multiple of the pivot row and return the reduced copy of the matrix.
