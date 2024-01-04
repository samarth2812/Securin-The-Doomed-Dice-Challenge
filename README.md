## The Doomed Dice Challenge
## Problem Statement
You are faced with the challenge of working with two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6. Your task is to analyze the combinations, distributions, and probabilities associated with rolling both dice together, and later tackle a more intricate problem involving reattaching spots to the dice.
## Part-A (15-20 Minutes):
Total Combinations:

Determine and showcase the total number of combinations possible when rolling both Die A and Die B together. Provide the mathematical explanation along with the implementation code.
Distribution of Combinations:

Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Represent the distribution as a 6 x 6 matrix. Include the mathematical explanation and code.
Probability of Sums:

Calculate the probability of all possible sums occurring among the number of combinations from the distribution. For each sum, express the probability as a fraction (e.g., P(Sum = 2) = 1/X). Provide the mathematical explanation and code.
## Part-B (25-30 Minutes):
Now, the challenge intensifies. While enjoying a board game with your dice, the mischievous Norse God Loki appears and dooms your dice by removing all the spots. Fortunately, you have the ability to reattach the spots, but Loki has set some conditions:

Die A cannot have more than 4 spots on a face.
Die A may have multiple faces with the same number of spots.
Die B can have as many spots on a face as necessary, even more than 6.
However, to continue playing your game, the probability of obtaining the sums must remain the same. Implement a transformation function undoom_dice that takes the original configurations of Die A and Die B as input and outputs new configurations that meet Loki's conditions while maintaining the original probability distribution.

## Input:
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A = [1, 2, 3, 4, 5, 6]
## Output:
A Transform Function undoom_dice that outputs:
New_Die_A = [?, ?, ?, ?, ?, ?]
New_Die_B = [?, ?, ?, ?, ?, ?]
Ensure that no New_Die_A[x] > 4
## Implementation
## Part-A:
Begin by calculating the total combinations of rolling both dice.
Create a 6 x 6 matrix to represent the distribution of combinations.
Calculate the probability of each sum and express it as a fraction.
## Part-B:
Define a function undoom_dice to reattach spots to the dice.
Explore various combinations while adhering to Loki's conditions.
Match the probability distribution of the new configurations with the original.
Ensure that Die A follows Loki's conditions (no more than 4 spots on a face).
Implement a clear and concise solution with comments for readability.
## Instructions for Running the Code
Ensure you have Python/Java/Ruby/C++/Go installed on your system. Execute the provided code snippets in a suitable environment.

Feel free to customize the code structure or add additional comments for better understanding.

## Acknowledgments
This challenge is designed to enhance your problem-solving skills, mathematical reasoning, and coding proficiency. Embrace the opportunity to tackle both straightforward and complex aspects of the problem.

Good luck! May your dice be ever in your favor.
