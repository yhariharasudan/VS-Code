import java.util.*;

public class factorial {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(Factorial(n));
}
public static int Factorial(int n)
{   
    if(n>1)
    {
        return n*Factorial(n-1);
    }
    else
     return 1;
}
}
