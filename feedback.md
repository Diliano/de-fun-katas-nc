# Feedback
## In this file, you will find feedback from a mentor for you to implement the following Wednesday.

### dna_pairs:
- Really comprehensive test suit and great use of a list comprehension to create your return value.
- When it comes to your test suite you've proven that your function can contain multi-length strings in the test `test_returns_multiple_pairs`, specifically with the input of `"AG"`, therefore I don't _think_ it's necessary to show that it works for `"ATAG"`. That being said, it's not necessary, but if it helps increase your confidence in your test suite, then it's worthwhile.

### get_tweet_data:
- What is the purpose of using a set for the mentions / tags?
- Your tests state `returns_correct_*****`-  I would suggest that 'correct' is arbitrary, and isn't exactly the point of the test. When we test, we're specifically looking at behaviours of the function, rather than the return value. I think a more accurate description would be something along the lines of `test_should_populate_length_property_on_dictionary`.

### Overall:
- Looking through your code, my feedback on the original two is applicable to most, if not all. Please make sure to go through and adjust your descriptions of tests.
- Your commit messages are very clear and have made my life so much easier, which is a big, big deal in development. Thank you!
