#! /usr/bin/env python

import re

words = " this is a test .,.,... this is a test. , test "

words = re.sub( '[r".,"]', '%', words )
print( words )

