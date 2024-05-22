// Java program for the above approach
import java.util.*;

class GFG{
	
// Recursive function to
// return GCD of a and b
static long gcd(long a, long b)
{
	if (a == 0)
		return b;
	else if (b == 0)
		return a;
	if (a < b)
		return gcd(a, b % a);
	else
		return gcd(b, a % b);
}
	
// Function to convert decimal to fraction
static void decimalToFraction(double number,double Q)
{

	// Fetch integral value of the decimal
	double intVal = Math.floor(number);

	// Fetch fractional part of the decimal
	double fVal = number - intVal;

	
	final long pVal = 1000000000;

	
	long gcdVal = gcd(Math.round(
					fVal * pVal), pVal);

	// Calculate num and deno
	long num = Math.round(fVal * pVal) / gcdVal;
	long deno = pVal / gcdVal;

    System.out.print((int)Q + " ");
	System.out.println((long)(intVal * deno) + 	num + "/" + deno);
}

public static void main(String s[])
{
	double X = 4.5;
    double N=X-Math.floor(X);
	decimalToFraction(N,Math.floor(X));
} 
}

