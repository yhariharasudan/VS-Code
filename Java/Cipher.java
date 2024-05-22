import java.util.*;
public class Cipher
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int i,j,k;
        System.out.println("Give a Encrypted string");
        String a=sc.nextLine();
        sc.close();
		ArrayList<Character> x=new ArrayList<Character>();
		ArrayList<Character> y=new ArrayList<Character>();
       char c[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        for(i=0;i<c.length;i++)
        {    x.add(c[i]);
            y.add(c[i]);}
        char C[]=a.toCharArray();
        System.out.println("Left Shift Possibilities");
  for(i=1;i<=25;i++)
   { 
     char d[]=new char[C.length];
      for(j=0;j<C.length;j++)
      {
        int z=0;
         z=x.indexOf(C[j]);
        z+=i;
        if(z>25)
        z-=26;
        if(x.contains(C[j]))
       d[j]=Character.toUpperCase(y.get(z));
       else 
       d[j]=' ';
      }
      for(k=0;k<d.length;k++)
      System.out.print(d[k]);
      System.out.println();
   }
   System.out.println("Right Shift Possibilities");
   for(i=1;i<=25;i++)
   { 
     char d[]=new char[C.length];
      for(j=0;j<C.length;j++)
      {
        int z=0;
         z=x.indexOf(C[j]);
        z-=i;
        if(z<0)
        z=26+z;
        if(x.contains(C[j]))
       d[j]=Character.toUpperCase(y.get(z));
       else
       d[j]=' ';
      }
      for(k=0;k<d.length;k++)
        System.out.print(d[k]);

  System.out.println();
}
}
}