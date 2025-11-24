Name: Drew N. Turgeon
Due Date: 11/25/2025
Class: COS 226
Teacher: Professor Schotter

Method 1: Linear Probing
1. This method has us look at the originally desired space that
the numerical equvilent of the string would like to go into. 
If that space is already occupied then the code will look at 
the next spot in the hash table and repeat the pattern. 
2. This method appears to average between 8.5 secs and 10.5 secs
for both title and quote.
3. This method has a high number of collisions with 87862536 for 
titles and 92779694 for quotes
4. Both of these sorting catagories provide no wasted space.
5. This method provides the benifit of using every space but With
the disadvantage of taking a long time with a lot of collisions.

Method 2: Non Probing
1. This method has us look at the originally desired space that 
the numerical equivelent of the string would like to go into. 
This method varies from the previous by giving up if the space is
already occupied and instead just returns collision.
2. This method averages under 0.1 secs for both titles and quotes.
3. This method has a lower number of collisions with 11245 for
titles and 12277 for quotes. 
4. Both of these sorting catagories provide waster space equal to
their collisions, that being 11245 and 12277.
5. This method has the advantage of being quick, but it also creates
a lot of wasted space and deletions which is exceptionally problematic.

Method 3: Quadratic Probing
1. This method has us look at the originally desired space that the 
numerical equivelent of the string would like to go into. This method
varies by using the formula ((key + (i * i)) % len(table)) to calculate 
the next position it will try. 
2. This method is also quite quck averaging less that 0.25 secs for
both titles and quotes.
3. This method does have a larger amount of collisions than the previous
with 1100938 for titles and 1163760 for quotes.
4. Both of these sorting catagories wasted four spots in the table.
5. This method has the advantage of being quick, though it is not as
fast as the previous, it has the advantage of having far less wasted
spaces.