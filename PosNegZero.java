import java.util.*;
 
class PosNegZero
{
    public static void main(String  args[])
    {
        int a;
        
        Scanner sc=new Scanner(System.in);
         
        System.out.print("Enter any integer number: ");
       
        if(a>0)
            System.out.println(a + " is POSITIVE NUMBER.");
        else if(a<0)
            System.out.println(a + " is NEGATIVE NUMBER.");
        else
            System.out.println("IT's ZERO.");
         
    }
}
