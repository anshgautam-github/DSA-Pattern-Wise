






Examples to FIND this pattern in the questions :


🔹 Step 1: Read the question carefully  :     “Check if array is sorted”
                          Hidden detail :     It doesn’t say ascending only    ,    It doesn’t say descending only
                           👉 That’s your FIRST HINT
                           
                           
🔹 Step 2: Identify possibilities    :     Ask yourself:   “In how many valid ways can this be true?”
                          Answer     :     Ascending ✅     Descending ✅     👉 So there are multiple valid conditions


🔹 Step 3: This triggers a pattern  :   Whenever you see:   “Output is true if condition A OR condition B”
                👉 You should think :
                                          boolean isA = true;
                                          boolean isB = true;
                                          This is not guessing — it's a standard reasoning pattern.
                                          

🔹 Step 4: Why initialize to true?      Because you are saying:   “I will assume it's valid unless I find a violation”   This is called:   👉 Assume valid → invalidate on conflict



🔹 When will this idea come to your mind?   Look for these signals in questions:
                                            🚨 Signal 1: “Check if array is sorted” (but no direction specified)
                                            🚨 Signal 2: “Return true if condition A OR B”
                                            🚨 Signal 3:  “Could belong to multiple types”
