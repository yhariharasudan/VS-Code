import java.util.*;
public class Arraylist {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n,d,q,x,y,i,j;
        n=sc.nextInt();
        ArrayList <ArrayList<Integer>> list=new ArrayList<ArrayList<Integer>>();
        
        for(i=0;i<n;i++)
        {
            d= sc.nextInt();
            ArrayList <Integer> a=new ArrayList<>(d);
            for(j=0;j<d;j++)
            {
                a.add(sc.nextInt());
            }
            list.add(a);
           // System.out.println(list);

        }

//System.out.println(list);
       q=sc.nextInt();
       for(i=0;i<q;i++)
       {
        x=sc.nextInt();
        y=sc.nextInt();
        try{
        System.out.println(list.get(x-1).get(y-1));}
        catch(IndexOutOfBoundsException e){
            System.err.println("Error");
        }
       }
       sc.close();
        



    }
}
