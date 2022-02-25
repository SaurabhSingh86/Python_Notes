import re

# ----------------------------------------------------------------------------------------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~  Characters   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
.   => Matches any character except new line
\.  => Matches a dot
\\  => Matches backslash
\*  => Matches astrick
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~   Character Set     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
[abcd]  =>  any character which matches either 'a' or 'b' or 'c' or 'd'
[^abcd] =>  any character but not 'a' or 'b' or 'c' or 'd'
[a-z]   =>  any character between 'a' through 'z'
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~ Special Sequences    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
\w  =>  word charcter. Same as [a-zA-Z0-9]. Matches alphanumeric and underscore
\W  =>  Non-word character. Same as [^a-zA-Z0-9]. Matches anything but word 
\d  =>  Matches a digit. Same as [0-9]
\D  =>  Matches a non-digit. Same as [^0-9]
\s  =>  Matches only whitespace
\S  =>  Matches only non-whitespace
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~  Anchors  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
^       =>  Start of string
$       =>  End of string
\b      =>  Word boudary
\B      =>  Not a word Boudary
[]      =>  Matches character in square brackets
[^ ]    =>  Matches character Not in square brackets
"""

# Method Charcters that needs to be Escaped (but need not be escaped when insi
"""
. ^ $ * + { } [ ] \ | ()
"""

# Qualifiers
"""
 *      =>  Matches expression 0 or more times
 +      =>  Matches expression 1 or more times
 ?      =>  Match expression 0 or 1 times
 {3}    =>  Matches expression exactly 3 times
 {3, 4} =>  Match expression 3 to 4 times
 {3, }  =>  Match expression 3 or more times
 { , 3} =>  Match expression 0 or 3 times
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Grouping      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
("A" | "B" | "C")   =>  Either "A" or "B" or "C"
"""
