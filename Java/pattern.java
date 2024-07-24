import java.util.*;

public class pattern {
    public static void main(String[] args) {
       // Scanner sc =new Scanner(System.in);
         int n=5,i,j;
        Righttriangle(n);
        
    }

    public static void  Righttriangle(int n)
    {
        int i,j,k;
        for(i=1;i<=n;i++)
        {
            for(k=1;k<=2*(n-i);k++)
            {
                System.out.print(" ");
            }
            for(j=1;j<i;j++)
            {
                System.out.print(j+" ");
            }
            for(j=i;j>0;j--)
            {
                System.out.print(j+" ");
            }
            System.out.println();
        }
     }


    public static void  triangle(int n)
    {
        for(i=1;i<=n;i++)
        {
           for(int k=1;k<=  2*(n-i);k++)
               {
                   System.out.print(" ");
               }
           for(j=1;j<= 2 * i -1;j++)
           {
               System.out.print(j +" ");
           }
           System.out.println();
        }

    }
    
}
