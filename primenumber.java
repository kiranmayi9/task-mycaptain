import java.util.Scanner;
public class prime
{                                                               //class declaration
        public static void main(String[] args)
	{	                                                //main method declaration
                Scanner sc=new Scanner(System.in);              //scanner class object creation

		System.out.println("Enter a number");
		int n = sc.nextInt();			        //taking a number n as input
		int count=0;
		for(int i = 1 ; i <=n ; i++)	
		{	
			if(n % i == 0)				//condition for getting the factors of number n
			count=count+1;
		}
		if(count == 2)		                        //if factors are two then, number is prime else not
		System.out.println("Prime Number");
		else
		System.out.println("Not a Prime Number");
		sc.close();		                        //closing scanner class(not mandatory but good practice)
	}                                                       //end of main method
}                                            
