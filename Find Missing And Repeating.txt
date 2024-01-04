class Solve {
    int[] findTwoElement(int a[], int n) {
        // code here
        int count[]=new int[n+1];
        int ans[]=new int[2];
        for(int i=0;i<count.length;i++)
        {
            count[i]=0;
        }
        for(int i=0;i<count.length;i++)
        {
            count[i]=0;
        }
        for(int i=0;i<a.length;i++)
        {
            count[a[i]]++;
        }
        for(int i=1;i<count.length;i++)
        {
            if(count[i]==0)
            {
                //System.out.println(a[i]);
                ans[1]=i;
            }
            else if(count[i]==2)
            {
                ans[0]=i;
            }
        }
        return ans;
    }
}