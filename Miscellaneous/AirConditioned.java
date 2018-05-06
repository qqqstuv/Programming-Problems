import java.util.*;

class AirConditioned {
  static char[] P;
	static char[] T;
	static int[] b;
	static int n, m;

  static class Pair implements Comparable<Pair>{
    int left;
    int right;
    Pair(int left, int right){
      this.left = left;
      this.right = right;
    }
    @Override
    public int compareTo(Pair pair2){
      int result =  Integer.compare(this.right, pair2.right);
      if (result == 0){
        return Integer.compare(this.left, pair2.left);
      }
      return result;
    }


  }

  public static int process(List<Pair> aList){
    int numRoom = 0;
    int tempMin = 0;
    for(int i = 0; i < aList.size(); i++){
      if(aList.get(i).left > tempMin){
        tempMin = aList.get(i).right;
        numRoom ++;
      }
    }
    // numRoom ++;
    return numRoom;
  }
 
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    in.nextLine();

    List<Pair> aList = new ArrayList<Pair>();

    while (in.hasNextLine()) {
      String[] S = in.nextLine().split(" ");
      int left = Integer.parseInt(S[0]);
      int right = Integer.parseInt(S[1]);
      aList.add(new Pair(left, right));
    }

    Collections.sort(aList);
    // for(int i = 0; i < aList.size(); i++){
    //     System.out.println("sorted " + aList.get(i).left + " " +  aList.get(i).right);
    // }
    int result = process(aList);
    System.out.println(result);
    // return process(aList);
  }
}