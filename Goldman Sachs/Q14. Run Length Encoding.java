class GfG
 {
	String encode(String s)
	{
        //Your code here
        String k="";
        int c=0;
        s=s+" ";
        for(int i=0; i<s.length()-1 ;i++)  
        {
            char ch1=s.charAt(i);
            char ch2=s.charAt(i+1);
            if(ch1==ch2)
            {
                c++;
            }
            else
            {
                k=k+ch1+(c+1);
                c=0;
            }
        }
        return k;
	}
	
 }