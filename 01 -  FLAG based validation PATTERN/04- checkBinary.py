# Check if Binary String is Alternating OR Same   Valid if: all same (0000 or 1111) OR alternating (0101)

public boolean checkBinary(String s) {
    boolean same = true;
    boolean alternating = true;

    for (int i = 0; i < s.length() - 1; i++) {
        if (s.charAt(i) != s.charAt(i + 1)) same = false;
        if (s.charAt(i) == s.charAt(i + 1)) alternating = false;
    }

    return same || alternating;
}
