# Palindrome

Given a string `s`, return `true` if is's palindrome, `false` otherwise. Uppercase => lowercase, remove all non-alpha charactars => forward = backward

- O(n) time
- O(1) space


> Let's think

The easy one is string == string[::-1]
Let's go deeper

First, we need to clean all the non-alpha. We'll iterate through the string (means N) and remove non-alpha (means save alpha)

Than we're going from left to right on our string with two flags, and s[i] should always be equal to s[j]. i++, j-- = till they are not equal. If we caught the problem = return False. Otherwise returh True

We can skip the checking!! Add it to the flags step. Let's code