import java.util.Scanner;

public class Fibanocci {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0;i<n;i++)
        {
            System.out.println(Fibanocci(i) + " ");
        }
    }
    public static int Fibanocci(int n)
    {
        if(n<=1)
        return n;
        else
        return Fibanocci(n-1) + Fibanocci(n-2);
    }

}
