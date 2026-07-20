class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        HashMap<Character, Character> hm = new HashMap<>();
        hm.put('[',']');
        hm.put('(', ')');
        hm.put('{', '}');
        for(int i = 0 ; i< s.length(); i++){
            if(hm.containsKey(s.charAt(i))){
                st.push(hm.get(s.charAt(i)));
            }
            else{
                if(st.isEmpty()){
                    return false;
                }
                char c = st.pop();

                if(s.charAt(i) != c){
                    return false;
                }
            }
        }

        return st.isEmpty();
    }
}
