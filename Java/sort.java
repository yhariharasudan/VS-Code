public class sort {
    public static void main(String[] args) {
        int a[]={5,4,3,2,1};
        int i,j,temp;
        for(i=0;i<5;i++)
        {
            for (j=i+1;j<5;j++)
            {
                  if(a[i]>a[j])
                  {
                    temp=a[j];
                    a[j]=a[i];
                    a[i]=temp;
                  }
            }
        }
        for(int k : a)
        {
            System.out.println(k);
        }
    }
    
}
