import java.util.*;

class AirConditioned {
  static char[] P;
	static char[] T;
	static int[] b;
	static int n, m;
 
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while (in.hasNextLine()) {
      String S = in.nextLine();
      if (S.equals(".")) break;
      P = S.toCharArray();
			T = (S+S).toCharArray();
			n = T.length;
			m = P.length;  		
  	
			kmpPreprocess();
			kmpSearch();
    }
  }
}