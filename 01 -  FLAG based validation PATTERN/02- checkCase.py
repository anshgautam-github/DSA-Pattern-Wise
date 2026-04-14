# Check if String is All Same Type ❓ Problem Check if string is: all lowercase OR all uppercase

public boolean checkCase(String s) {
    boolean lower = true, upper = true;

    for (char c : s.toCharArray()) {
        if (!Character.isLowerCase(c)) lower = false;
        if (!Character.isUpperCase(c)) upper = false;
    }

    return lower || upper;
}
