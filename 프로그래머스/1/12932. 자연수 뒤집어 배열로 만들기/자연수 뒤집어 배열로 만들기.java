class Solution {
    public int[] solution(long n) {
        
        String num = String.valueOf(n);
        int[] answer = new int[num.length()];
        for(int i=0; i<answer.length; i++){
            answer[i]=(int)(n%10);
            n/=10;
        }
        return answer;
    }
}