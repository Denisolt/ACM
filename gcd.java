public class gcd {
	public static void main(String []args)
	{
		gcdcalc(1298, 561);
		System.out.println();
		System.out.println();
		gcdcalc(1534, 663);
	}
	public static int gcdcalc(int a, int b)
	{	
		System.out.println("a = " + a + "	b = " + b + "		r = mod(r1,r2)");
		System.out.println("______________________________________________________");
		int gcd = 0;
		if((a <= 0||(b<=0)))
			return gcd;
		if(b>a)
			return gcd;
		int r1=a;
		int r2=b;
		int r = r1%r2;
		while(r>0)
		{
			r1=r2;
			r2=r;
			r = r1%r2;
			System.out.println("    " + r1 + "	    	" + r2 + "		   " + r );
		System.out.println("______________________________________________________");
		}
		if(r==0)
			gcd = r2;
		System.out.println("gcd: " + gcd);
		return gcd;

	}
}