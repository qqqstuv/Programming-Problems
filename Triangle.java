/**
 * Created by ducn on 5/17/17.
 */
import java.math.BigDecimal;
import java.util.*;

public class Triangle {

  public Triangle(){

  }

  private static int compute(int n){
    BigDecimal base =  (new BigDecimal(1.5).pow(n));
    base = base.multiply(new BigDecimal(3));
    System.out.println(base.doubleValue());
    int length = (int)(base.log
    return length;
  }
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int count = 1;
    while(sc.hasNext()){
      int i = Integer.parseInt(sc.nextLine());
      int length = compute(i);
      System.out.println("Case " + count + ": " + length);
      count++;
    }

  }
}
